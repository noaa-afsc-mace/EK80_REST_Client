# coding=utf-8
#
#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaska Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)
#
#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.
#
"""
.. module:: ek80_rest_client.ek80_rest_client

    :synopsis: ek80_rest_client provides a simplified interface for
               the EK80 application REST server.

| Developed by:  Rick Towler   <rick.towler@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
"""


'''
http://192.168.56.5:45123/swagger/
'''

import datetime
import zmq
import numpy as np
import ek80_data_client
import ek80_param_client
from google.protobuf.json_format import MessageToDict
import ek80_datagrams_v2360_pb2 as ek80_datagrams_pb2
#from PyQt5 import QtCore
from PyQt6 import QtCore


class ek80_rest_client(QtCore.QObject):

    #  set the zmq message polling interval in ms
    ZMQ_POLL_INTERVAL = 10

    # Create a constant to convert indexed power to power.
    INDEX2POWER = (10.0 * np.log10(2.0) / 256.0)

    #  define our signals
    subscriptionData = QtCore.pyqtSignal(object, str, dict)
    cleanupComplete = QtCore.pyqtSignal()


    def __init__(self, name, server_address='localhost', param_server_port=12345,
            data_server_port=12346, end_point_port=24240, request_timeout=5,
            parent=None):

        super(ek80_rest_client, self).__init__(parent)

        #  clients must have unique names. Client names are used in creating endpoints
        #  and this name will be used to manage these endpoints and their subscriptions.
        #  If this name is NOT unique,
        self.name = str(name)

        #  initialize some attributes
        self.endpoints = {}
        self.subscriptions = {}
        self.n_subscriptions = 0
        self.next_server_port = end_point_port
        self.server_address = server_address
        self.request_timeout = request_timeout

        #  THIS IS A HACK - It appears that the URLACLs created when the EK80 Web API
        #  is configured for localhost literally have "localhost" as the host name and thus the
        #  host strings created below MUST use 'localhost' as the hostname. BUT - you can't
        #  seemingly use 'localhost' as the hostname when creating an endpoint so for endpoints
        #  we need to use 127.0.0.1. This only comes into play when the EK80 Web API access is
        #  configured for "Echosounder PC" (i.e. localhost access only)
        if self.server_address == '127.0.0.1':
            server_address = 'localhost'
        elif self.server_address == 'localhost':
            self.server_address == '127.0.0.1'

        #  create instances of our ek80_data_client and ek80_parameter_clients
        self.param_client_config = ek80_param_client.Configuration()
        self.param_client_config.host="http://" + server_address + ":" + str(param_server_port) + "/"
        self.param_api_client = ek80_param_client.ApiClient(configuration=self.param_client_config)
        self.data_client_config = ek80_data_client.Configuration()
        self.data_client_config.host="http://" + server_address + ":" + str(data_server_port) + "/"
        self.data_api_client = ek80_data_client.ApiClient(configuration=self.data_client_config)

        #  create a timer to poll the zero-mq subscriptions
        self.poll_timer = QtCore.QTimer(self)
        self.poll_timer.timeout.connect(self.poll_zmq_messages)


    def get_channels(self):
        '''
        get_channels returns a list containing the installed echosounder channels
        '''
        pca = ek80_param_client.PingConfigurationApi(self.param_api_client)
        return pca.ping_configuration_get_channels(_request_timeout=self.request_timeout)


    def get_water_column_environment(self):
        '''
        get_water_column_environment returns a dictionary containing the water column
        environment data.

            acidity                                     float
            depth_for_sv_and_absorption_calculations    float
            latitude_for_pressure_calculations          float
            salinity                                    float
            water_temperature                           float
            water_column_sound_speed_source             str
            water_column_sound_speed                    float
            selected_profile                            str


        '''

        ea = ek80_param_client.EnvironmentApi(self.param_api_client)
        return ea.environment_get_water_column_data(_request_timeout=self.request_timeout)


    def get_transducer_face_environment(self):
        '''
        get_transducer_face_environment returns a dictionary containing the transducer face
        environment data.

            transducer_sound_speed_source               str
            transducer_manual_sound_speed               float
        '''

        ea = ek80_param_client.EnvironmentApi(self.param_api_client)
        return ea.environment_get_transducer_face_data(_request_timeout=self.request_timeout)


    def get_navigation(self):
        '''
        get_navigation returns the current lat/lon, course, speed, heading, and vessel log
        '''

        osa = ek80_param_client.OwnshipApi(self.param_api_client)
        return osa.ownship_get_navigation(_request_timeout=self.request_timeout)


    def get_motion(self):
        """
        get_motion returns heave, pitch, roll, surge, sway, time, and yaw (heading)
        """
        osa = ek80_param_client.OwnshipApi(self.param_api_client)
        motion_data = osa.ownship_get_motion(_request_timeout=self.request_timeout)

        #convert the ping_time to a datetime
        motion_data.time = self.convert_nt_time(motion_data.time)

        return motion_data


    def get_operation_mode(self):
        """
        get_operation_mode returns...
        """
        sa = ek80_param_client.SystemApi(self.param_api_client)
        return sa.system_get_operation_mode(_request_timeout=self.request_timeout)


    def set_operation_mode(self, mode):
        '''
        set_operation_mode sets...
        '''
        sa = ek80_param_client.SystemApi(self.param_api_client)
        sa.system_put_operation_mode(mode, _request_timeout=self.request_timeout)


    def get_operational_state(self):
        """
        get_operational_state returns...
        """
        sa = ek80_param_client.SystemApi(self.param_api_client)
        return sa.system_get_operational_state(_request_timeout=self.request_timeout)


    def get_ping_interval(self):
        """
        get_ping_interval returns...
        """
        sa = ek80_param_client.SystemApi(self.param_api_client)
        return sa.system_get_ping_interval(_request_timeout=self.request_timeout)


    def set_ping_interval(self, interval):
        '''
        set_ping_interval sets...
        '''
        sa = ek80_param_client.SystemApi(self.param_api_client)
        sa.system_put_ping_interval(interval, _request_timeout=self.request_timeout)


    def get_ping_mode(self):
        """
        get_ping_mode returns...
        """
        sa = ek80_param_client.SystemApi(self.param_api_client)
        return sa.system_get_ping_mode(_request_timeout=self.request_timeout)


    def set_ping_mode(self, mode):
        '''
        set_ping_mode sets...
        '''
        sa = ek80_param_client.SystemApi(self.param_api_client)
        sa.system_put_ping_mode(mode, _request_timeout=self.request_timeout)


    def get_recording_range(self, channel_id):
        """
        get_recording_range returns the current recording range for the
        provided channel. It also returns the state of the channel's auto
        recording range setting.

        This method only returns meaningful data when individual recording
        ranges are configured. If the channel recording range is set to
        Common, calls to this method return a a default IndividualRangeControl
        object.
        """
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)
        return dsa.data_storage_ek80_get_individual_channel_range(channel_id,
                _request_timeout=self.request_timeout)


    def set_recording_range(self, channel_id, range, auto_range=False):
        '''
        set_recording_range sets the recording range for the specified channel.
        You can set auto_range to True to enable automatic recording range.
        '''
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)
        channel_range = ek80_param_client.IndividualRangeControl(channel_id=channel_id,
                individual_channel_range=range, individual_channel_auto=auto_range)
        dsa.data_storage_ek80_set_individual_channel_range(channel_range,
                _request_timeout=self.request_timeout)


    def get_recording_settings(self):
        """
        get_recording_settings returns the current Raw data recording settings in
        a MainStorageSettings object.

        Attribute                   Type
        file_path                   str
        raw_file_name_prefix        str
        max_file_size (bytes)       int
        min_free_disk_space (bytes) int
        sample_range (m)            int
        sample_range_auto           bool
        individual_range_control    bool
        record_raw_active           bool
        sample_data_format_wbt_cw   str
            sample_data_format_wbt_cw values:
                'complex'
                'power-angle'
                'power-angle-decimated'

        """
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)
        record_settings = dsa.data_storage_get_basic_storage_settings(_request_timeout=self.request_timeout)

        #  as of EK80 23.6.2 the data_storage_get_basic_storage_settings() call always returns
        #  True for record_raw_active regardless of the record button state. But, the
        #  data_storage_get_record_raw_active() returns the correct state so we use
        #  that call to correct the value returned from data_storage_get_basic_storage_settings()
        record_settings.record_raw_active = dsa.data_storage_get_record_raw_active(_request_timeout=self.request_timeout)

        return record_settings


    def set_recording_settings(self, path=None, file_prefix=None,
            max_file_size=None, min_free_disk_space=None, record_range=None,
            record_range_auto=None, individual_range_control=None,
            record_active=None, sample_data_format_wbt_cw=None):
        '''
        set_recording_settings sets a number of general data recording
        parameters.
        '''
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)

        #  while the EK80 REST API docs say that all arguments to MainStorageSettings
        #  are optional, they are not really that optional. If you fail to provide an
        #  option, None is passed and EK80 reverts to a default value for that parameter.
        #  This happens at the MainStorageSettings class also so passing None here isn't
        #  the problem. This issue probably exists across the library and so we need to
        #  identify where this is an issue and provide a workaround such that the user
        #  doesn't need to provide all parameters at every call.


        #  in light of the above, we will get the current settings
        current_settings = self.get_recording_settings()

        #  populate any omitted args with the current active values
        if path is None:
            path = current_settings.file_path
        if file_prefix is None:
            file_prefix = current_settings.raw_file_name_prefix
        if max_file_size is None:
            max_file_size = current_settings.max_file_size
        if min_free_disk_space is None:
            min_free_disk_space = current_settings.min_free_disk_space
        if record_range is None:
            record_range = current_settings.sample_range
        if record_range_auto is None:
            record_range_auto = current_settings.sample_range_auto
        if individual_range_control is None:
            individual_range_control = current_settings.individual_range_control
        if record_active is None:
            record_active = current_settings.record_raw_active
        if sample_data_format_wbt_cw is None:
            sample_data_format_wbt_cw = current_settings.sample_data_format_wbt_cw

        #  create a storage settings object that is fully populated
        storage_settings = ek80_param_client.MainStorageSettings(file_path=path,
                raw_file_name_prefix=file_prefix,
                max_file_size=max_file_size,
                min_free_disk_space=min_free_disk_space,
                sample_range=record_range,
                sample_range_auto=record_range_auto,
                individual_range_control=individual_range_control,
                record_raw_active=record_active,
                sample_data_format_wbt_cw=sample_data_format_wbt_cw)
        dsa.data_storage_set_basic_storage_settings(storage_settings,
                _request_timeout=self.request_timeout)


    def get_recording_state(self):
        '''
        get_recording_state returns True if the EK80 software is recording raw
        data to disk and False if it is not.
        '''
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)
        return dsa.data_storage_get_record_raw_active(_request_timeout=self.request_timeout)


    def set_recording_state(self, enabled):
        '''
        set_recording_state sets the raw data recording state. True enables
        recording and False stops it.
        '''
        dsa = ek80_param_client.DataStorageApi(self.param_api_client)
        dsa.data_storage_set_record_raw_active(bool(enabled), _request_timeout=self.request_timeout)


    def get_drop_keel_offset(self):
        '''
        get_drop_keel_offset returns the current drop keel setting value and a bool
        indicating the value is manually set.
        '''
        osa = ek80_param_client.OwnshipApi(self.param_api_client)
        return osa.ownship_get_drop_keel_offset(_request_timeout=self.request_timeout)


    def set_drop_keel_offset(self, new_offset):
        '''
        set_drop_keel_offset sets the current drop keel value and a bool
        indicating the value is manually set.
        '''
        osa = ek80_param_client.OwnshipApi(self.param_api_client)
        dropkeel_settings = ek80_param_client.ManualSetting(current_value=new_offset,
                is_manual=True)
        osa.ownship_set_drop_keel_offset(dropkeel_settings, _request_timeout=self.request_timeout)


    def get_ping_configuration(self):
        '''
        get_ping_configuration returns...
        '''
        pca = ek80_param_client.PingConfigurationApi(self.param_api_client)
        return pca.ping_ek80_configuration_get_ping_configuration(_request_timeout=self.request_timeout)


    def get_channel_transmit_power(self, channel_id):
        '''
        get_channel_transmit_power returns...
        '''
        pca = ek80_param_client.PingConfigurationApi(self.param_api_client)
        return pca.ping_configuration_get_channel_transmit_power(channel_id,
                _request_timeout=self.request_timeout)


    def get_channel_pulse_settings(self, channel_id):
        '''
        get_channel_pulse_settings returns...
        '''
        pca = ek80_param_client.PingConfigurationApi(self.param_api_client)
        return pca.ping_configuration_get_channel_pulse_settings(channel_id,
                _request_timeout=self.request_timeout)


    def delete_bottom_detection_subscription(self, sub_id, endpoint_id=None,
            cleanup=False):
        '''
        delete_bottom_detection_subscription deletes the specified bottom
        detection subscription. It also disconnects the subscription from
        its endpoint. IT DOES NOT DELETE THE ENDPOINT.

        Args:
            sub_id (int):
                The subscription ID of the bottom detection subscription
                you are deleting.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.
        '''
        #  check if this is a valid subscription and if it is a bottom detection sub.
        #  we skip this check if we're cleaning up
        if not cleanup:
            if sub_id not in self.subscriptions:
                raise ValueError('%i is not a valid subscription id' % (sub_id))
            if self.subscriptions[sub_id]['type'] != 'bottom detection':
                raise ValueError('Error deleting bottom detector subscription. ' +
                        'Subscription %i is not a bottom detection subscription.' % (sub_id))

        #  get the endpoint ID
        if endpoint_id is None:
            endpoint_id = self.subscriptions[sub_id]['endpoint_id']

        #  remove the subscription from its endpoint
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)
        api_instance.remove_subscription_from_end_point(endpoint_id, sub_id)

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  delete the bottom detection subscription
        api_instance.delete_bottom_detection_subscription(sub_id)

        #  update the endpoint's subscriptions list and remove the subscription
        #  from our subscriptions dict.
        if not cleanup:
            self.endpoints[endpoint_id]['subscriptions'].remove(sub_id)
            del self.subscriptions[sub_id]


    def get_bottom_detection_subscription(self, sub_id):
        '''

        Args:
            sub_id (int):
                The subscription ID of the bottom detection subscription
                you are requesting the state of.

        Returns:
            Dictionary with the following fields:

                    subscription_id (int)
                    channel_id (str)
                    subscription_name (str)
                    subscriber_name (str)
                    upper_detector_limit (float)
                    lower_detector_limit (float)
                    bottom_back_step (float)

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.

        '''

        #  check if this is a valid subscription and if it is a bottom detection sub.
        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))
        if self.subscriptions[sub_id]['type'] != 'bottom detection':
            raise ValueError('Error getting bottom detector subscription configuration. ' +
                    'Subscription %i is not a bottom detection subscription.' % (sub_id))

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  and use it to update our subscription
        sub_spec = api_instance.get_bottom_detection_subscription(sub_id)

        #  create the return dict
        settings = {'subscription_id':sub_id,
                    'channel_id': sub_spec.channel_id,
                    'subscription_name':sub_spec.subscription_name,
                    'subscriber_name': sub_spec.subscriber_name,
                    'upper_detector_limit':sub_spec.settings.upper_detector_limit,
                    'lower_detector_limit': sub_spec.settings.lower_detector_limit,
                    'bottom_back_step':sub_spec.settings.bottom_back_step
                    }

        return settings


    def update_bottom_detection_subscription(self, sub_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50):
        '''

        Args:
            sub_id (TYPE):
                DESCRIPTION
            upper_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 10.
            lower_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 1000.
            bottom_back_step (TYPE):
                Optional; DESCRIPTION Defaults to -50.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.
        '''

        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))

        if self.subscriptions[sub_id]['type'] != 'bottom detection':
            raise ValueError('Error updating bottom detector subscription. Subscription ' +
                    '%i is not a bottom detection subscription' % (sub_id))

        #  create a bottom detection settings obj
        sub_settings = ek80_data_client.BottomDetectionSettings()

        #  set the various properties
        sub_settings.upper_detector_limit = upper_detector_limit
        sub_settings.lower_detector_limit = lower_detector_limit
        sub_settings.bottom_back_step = bottom_back_step

        #  create an instance of the bottom detections subs api
        api_instance = ek80_data_client.BottomDetectionSubscriptionsApi(self.data_api_client)

        #  and use it to update our subscription
        api_instance.update_bottom_detection_subscription(sub_id, sub_settings)


    def create_bottom_detection_subscription(self, channel_id, upper_detector_limit=10,
            lower_detector_limit=1000, bottom_back_step=-50, name=None, endpoint_id=None):
        '''

        Args:
            channel_id (TYPE):
                DESCRIPTION
            upper_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 10.
            lower_detector_limit (TYPE):
                Optional; DESCRIPTION Defaults to 1000.
            bottom_back_step (TYPE):
                Optional; DESCRIPTION Defaults to -50.
            name (TYPE):
                Optional; DESCRIPTION Defaults to None.
            endpoint_id (TYPE):
                Optional; DESCRIPTION Defaults to None.

        Returns:
            The subscription ID as int

        '''

        #  increment the subscription counter
        self.n_subscriptions += 1

        #  if a subscription name is provided, use it, otherwise create one.
        #  The subscription name must be unique.
        if name:
            name = str(name)
        else:
            name = "%i-bottom detection" % (self.n_subscriptions)

        #  check if we've been provided an endpoint to use. If not, generate one.
        if endpoint_id not in self.endpoints:
            endpoint_id = self.create_server_endpoint()

        #  create an instance of the create subscription API
        api_instance = ek80_data_client.CreateADataSubscriptionApi(self.data_api_client)

        #  create our settings and spec objects
        sub_settings = ek80_data_client.BottomDetectionSettings()
        sub_spec = ek80_data_client.BottomDetectionSubscriptionSpecification()

        #  set the various properties
        sub_settings.upper_detector_limit = upper_detector_limit
        sub_settings.lower_detector_limit = lower_detector_limit
        sub_settings.bottom_back_step = bottom_back_step
        sub_spec.channel_id = channel_id
        sub_spec.settings = sub_settings
        sub_spec.subscriber_name = self.name
        sub_spec.subscription_name = name

        #  create the subscription
        sub_id = api_instance.create_bottom_detection_subscription(sub_spec)

        #  add this sub to the subscriptions dict
        self.subscriptions[sub_id] = {'name':name, 'channel_id':channel_id,
                'endpoint_id':endpoint_id, 'type':'bottom detection',
                'cleanup':self.delete_bottom_detection_subscription}

        #  and connect the subscription to the endpoint
        subscription_output_args = ek80_data_client.SubscriptionOutputArgs(sub_id, 'proto-buf')
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)
        api_instance.add_subscription_to_end_point(endpoint_id, subscription_output_args)
        self.endpoints[endpoint_id]['subscriptions'].append(sub_id)

        return sub_id


    def poll_zmq_messages(self):
        '''
        poll_zmq_messages periodically checks all endpoints for available messages.
        If messages are available, they are received, unpacked, and the message data
        is emitted using the subscriptionData signal.

        Returns:
            None

        '''

        #  poll each of our endpoints
        for endpoint_id in self.endpoints:

            #  check if a message is available
            try:
                has_msg = self.endpoints[endpoint_id]['zmq_socket'].poll(timeout=0)
            except:
                continue
            if has_msg == zmq.POLLIN:
                #  a message is available - get it. The protobuf zmq messages
                #  are multipart where the first part is the message type
                #  and the second is the serialized protobuf data
                msg = self.endpoints[endpoint_id]['zmq_socket'].recv_multipart()

                #  process the message based on the type - THIS MUST BE
                #  EXTENDED AS NEW TYPES ARE ADDED TO THE CLIENT
                if msg[0].decode("utf-8") == 'Bot.PB.v1':
                    try:
                        #  set the type
                        data_type = 'bottom detection'
                        dg_dict = {}

                        #  create the protobuf object and decode
                        dg_data = ek80_datagrams_pb2.BottomDetectionDatagram()
                        dg_data.ParseFromString(msg[1])

                        #  convert the message obj to a dict
                        dg_dict = MessageToDict(dg_data)

                        #  and convert the ping_time to a datetime
                        dg_dict['pingTime'] = self.convert_nt_time(dg_dict['pingTime'])

                        #  convert subscription ID to int
                        dg_dict['subscriptionId']  = int(dg_dict['subscriptionId'])

                        #  at least with the initial 21.15 REST client, bottom detection
                        # subscriptions return "test" as the dataSource - we'll fix that here
                        dg_dict['dataSource'] = self.subscriptions[dg_dict['subscriptionId']]['channel_id']

                        #  emit the data signal
                        self.subscriptionData.emit(self, data_type, dg_dict)
                    except:
                        #  There was a problem parsing the datagram.
                        #  For now we just drop datagrams that we can't parse
                        pass

                elif msg[0].decode("utf-8") == 'Eco.PB.v1':
                    try:
                        #  set the type
                        data_type = 'echogram'
                        dg_dict = {}

                        #  create the protobuf object and decode
                        dg_data = ek80_datagrams_pb2.EchogramDatagram()
                        dg_data.ParseFromString(msg[1])

                        #  convert the message obj to a dict
                        dg_dict = MessageToDict(dg_data)

                        #  and convert the ping_time to a datetime
                        dg_dict['pingTime'] = self.convert_nt_time(dg_dict['pingTime'])

                        #  convert subscription ID to int
                        dg_dict['subscriptionId']  = int(dg_dict['subscriptionId'])

                        #  check for a depth field and insert if missing. The depth
                        #  field is omitted if there is no bottom detection.
                        if 'bottomDepth' not in dg_dict:
                            dg_dict['bottomDepth'] = 0

                        #  convert EK500 dB format?
                        if not self.subscriptions[dg_dict['subscriptionId']]['return_db_format']:
                            #  yes, return Sv as float
                            dg_dict['data'] = np.array(dg_dict['data'], dtype=np.single)
                            dg_dict['data'] *= self.INDEX2POWER
                        else:
                            #  return EK500 dB format data as 16-bit int
                            dg_dict['data'] = np.array(dg_dict['data'], dtype=np.short)

                        #  emit the data signal
                        self.subscriptionData.emit(self, data_type, dg_dict)
                    except:
                        #  There was a problem parsing the datagram.
                        #  For now we just drop datagrams that we can't parse
                        pass

                else:
                    #  This is an unknown type - print the type
                    print('New message type: ' +  msg[0].decode("utf-8"))
                    print('You must add this type to the poll_zmq_messages() method of the EK80 client.')


    @QtCore.pyqtSlot()
    def cleanup_client(self, quiet=False):
        '''
        cleanup_client should be called when you're done using the client
        to ensure that all of the client's subscriptions and endpoints
        are deleted from the server.

        If you do not call this method, or your application crashes without
        calling it, any subscriptions and endpoints you created will remain
        active on the server and the endpoint address(es) will be unavailable
        for new endpoints.

        '''

        #  stop the polling timer if it is running
        if self.poll_timer.isActive():
            self.poll_timer.stop()

        #  delete all existing subscriptions - since we may be trying
        #  to delete subscriptions that don't exist, we ignore any errors
        for sub_id in self.subscriptions:
            try:
                self.subscriptions[sub_id]['cleanup'](sub_id, cleanup=True)
            except:
                pass

        #  and remove all existing endpoints - since we may be trying
        #  to remove endpoints that don't exist, we ignore any errors
        for endpoint_id in self.endpoints:
            try:
                self.delete_server_endpoint(endpoint_id)
            except:
                pass

        self.subscriptions = {}
        self.endpoints = {}

        if not quiet:
            self.cleanupComplete.emit()


    def cleanup_server(self, clean_all=False):
        '''
        cleanup_server removes subscriptions and endpoints associated with
        this instance of the EK80 client from the EK80 server.

        A properly working client application should call cleanup_client()
        and clean up after itself so you normally shouldn't need to call this
        method. But during development it is common for your application to
        crash, leaving subscriptions and endpoints strewn about the server.
        You can call this method before making any subscriptions to clean
        these up.

        Args:
            clean_all (bool): Set this to True to remove ALL subscriptions
                    and endpoints from the EK80 server. This should be used
                    with caution when running more than one rest client
                    application since this would kill subscriptions for those
                    other apps.

                Default: False

        Returns:
            None

        '''

        #  stop the polling timer if it is running
        if self.poll_timer.isActive():
            self.poll_timer.stop()

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  get a list of all active endpoints
        endpoints = api_instance.get_active_communication_end_points()

        #  worth thru the endpoints
        for endpoint in endpoints:
            #  get the endpoint id
            endpoint_id = endpoint.communication_end_point_id

            #  check if we're cleaning up endpoints by name
            if not clean_all:
                #  we are, check if our name is in this endpoint's name
                if self.name not in endpoint.name:
                    #  it is not, skip
                    continue

            #  get a list of subs associated with this endpoint
            subscriptions = api_instance.get_subscriptions_by_end_point(endpoint_id)

            #  work thru the subscriptions, deleting them as we go
            for sub in subscriptions:
                #  as we add new subscription types, we need to expand this code
                #  to handle deleting them.
                if sub.subscription_type == 'bottom detection':
                    self.delete_bottom_detection_subscription(sub.subscription_id,
                            endpoint_id=endpoint_id, cleanup=True)

                elif sub.subscription_type == 'echogram':
                    self.delete_echogram_subscription(sub.subscription_id,
                            endpoint_id=endpoint_id, cleanup=True)

                else:
                    print("New subscription type found: " + sub.subscription_type)
                    print("ek80_rest_client.cleanup_server() NEEDS TO BE " +
                            "UPDATED TO HANDLE THIS TYPE!")

            #  and delete the endpoint
            api_instance.delete_communication_end_point(endpoint_id)

        self.subscriptions = {}
        self.endpoints = {}


    def delete_server_endpoint(self, endpoint_id):
        '''

        Args:
            endpoint_id (TYPE):
                DESCRIPTION

        Returns:
            None

        Raises:
            ValueError: DESCRIPTION
        '''

        #  check if this is a valid endpoint
        if endpoint_id not in self.endpoints:
            raise ValueError('%i is not a valid endpoint id' % (endpoint_id))

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  and delete the endpoint
        api_instance.delete_communication_end_point(endpoint_id)


    def create_server_endpoint(self, name=None):
        '''
        create_server_endpoint is an internal method that creates an endpoint
        on the server. Think of an endpoint as a socket where data from subscriptions
        is sent. Multiple subscriptions can share an endpoint.

        Args:
            name (TYPE):
                Optional; A unique name for the endpoint. If no name is passed
                a name will be generated. Defaults to None.

        Returns:
        {0}int: The endpoint id

        '''

        #  set the endpoint name - this must be unique for each endpoint
        if name:
            name = str(name)
        else:
            #  generate a unique name using the client name and server port
            name = self.name + '-' + str(self.next_server_port)

        #  create an instance of the CommunicationEndPoints API
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        #  craft the endpoint address string
        endpoint = 'tcp://' + self.server_address + ':' + str(self.next_server_port)

        #  create an instance of the end point settings object. This client always
        #  uses the zero-mq messaging system which as of 21.15 is the only system
        #  that is implemented.
        com_settings = ek80_data_client.CommunicationEndPointSettings(name, endpoint, 'zero-mq')

        #  create the endpoint - this returns the endpoint ID
        endpoint_id = api_instance.create_communication_end_point(com_settings)

        #  create the zmq subscriber for this endpoint
        zmq_context = zmq.Context()
        zmq_sock = zmq_context.socket(zmq.SUB)
        zmq_sock.connect (endpoint)
        zmq_sock.setsockopt(zmq.SUBSCRIBE, b'')

        #  add this endpoint to the endpoints dict
        self.endpoints[endpoint_id] = {'endpoint':endpoint, 'zmq_context':zmq_context,
                'zmq_socket':zmq_sock, 'subscriptions':[]}

        #  check if we're polling and if not, start
        if not self.poll_timer.isActive():
            self.poll_timer.start(self.ZMQ_POLL_INTERVAL)

        #  increment the server port
        self.next_server_port += 1

        #  return the endpoint id
        return endpoint_id


    def convert_nt_time(self, nt_time):
        '''
        convert_nt_time is an internal function that converts 64-bit "NT" time
        (an integer specifying the number of 100-nanosecond intervals which have
        passed since January 1, 1601) to Unix time (number of seconds that have
        elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1
        January 1970)

        The input 64-bit value is split into the two 32 bits "l" and "h"
        '''
        #  difference between 1601 and 1970
        d = 116444736000000000

        #  shift and divide by 10 million to convert to seconds
        ts = (int(nt_time) - d) / 10000000.0

        return datetime.datetime.fromtimestamp(ts)



    def delete_echogram_subscription(self, sub_id,  endpoint_id=None,
            cleanup=False):
        '''
        delete_echogram_subscription deletes the specified echogram subscription.
        It also disconnects the subscription from its endpoint. IT DOES NOT
        DELETE THE ENDPOINT.

        Args:
            sub_id (int):
                The subscription ID of the echogram subscription
                you are deleting.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a echogram subscription.
        '''
        #  check if this is a valid subscription and if it is a bottom detection sub.
        #  we skip this check if we're cleaning up
        if not cleanup:
            if sub_id not in self.subscriptions:
                raise ValueError('%i is not a valid subscription id' % (sub_id))
            if self.subscriptions[sub_id]['type'] != 'echogram':
                raise ValueError('Error deleting echogram subscription. ' +
                        'Subscription %i is not an echogram subscription.' % (sub_id))

        #  get the endpoint ID
        if endpoint_id is None:
            endpoint_id = self.subscriptions[sub_id]['endpoint_id']

        #  remove the subscription from its endpoint
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)

        try:
            api_instance.remove_subscription_from_end_point(endpoint_id, sub_id)
        except:
            pass

        #  create an instance of the echogram subs api
        api_instance = ek80_data_client.EchogramSubscriptionsApi(self.data_api_client)

        #  delete the echogram subscription
        try:
            api_instance.delete_echogram_subscription(sub_id)
        except:
            pass

        #  update the endpoint's subscriptions list and remove the subscription
        #  from our subscriptions dict.
        if not cleanup:
            self.endpoints[endpoint_id]['subscriptions'].remove(sub_id)
            del self.subscriptions[sub_id]


    def get_echogram_subscription(self, sub_id):
        '''

        Args:
            sub_id (int):
                The subscription ID of the echogram subscription
                you are requesting the state of.

        Returns:
            Dictionary with the following fields:

                    subscription_id (int)
                    channel_id (str)
                    subscription_name (str)
                    subscriber_name (str)
                    pixel_count (float)
                    range (float)
                    range_start (float)
                    tvg_function (float)
                    bottom_gain (float)
                    tvg_type (str)
                    bottom_tvg_type (str)
                    echogram_type (str)
                    compression_type (str)
                    expansion_type (str)
                    echogram_heave (int)
                    echogram_ping_filter_state(int)
                    echogram_min_pixel_value (float)
                    echogram_transducer_depth(int)
                    echogram_delay(int)


        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.

        '''

        #  check if this is a valid subscription and if it is a echogram sub.
        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))
        if self.subscriptions[sub_id]['type'] != 'echogram':
            raise ValueError('Error getting echogram subscription configuration. ' +
                    'Subscription %i is not an echogram subscription.' % (sub_id))

        #  create an instance of the echogram sub api
        api_instance = ek80_data_client.EchogramSubscriptionsApi(self.data_api_client)

        #  and use it to get our subscription info
        sub_spec = api_instance.get_echogram_subscription(sub_id)

        #  create the return dict
        settings = {'subscription_id':sub_id,
                    'channel_id': sub_spec.channel_id,
                    'subscription_name':sub_spec.subscription_name,
                    'subscriber_name': sub_spec.subscriber_name,
                    'pixel_count':sub_spec.settings.pixel_count,
                    'range':sub_spec.settings.range,
                    'range_start':sub_spec.settings.range_start,
                    'tvg_function':sub_spec.settings.tvg_function,
                    'bottom_gain':sub_spec.settings.bottom_gain,
                    'tvg_type':sub_spec.settings.tvg_type,
                    'bottom_tvg_type':sub_spec.settings.bottom_tvg_type,
                    'echogram_type':sub_spec.settings.echogram_type,
                    'compression_type':sub_spec.settings.compression_type,
                    'expansion_type':sub_spec.settings.expansion_type,
                    'echogram_heave':sub_spec.settings.echogram_heave,
                    'echogram_ping_filter_state':sub_spec.settings.echogram_ping_filter_state,
                    'echogram_min_pixel_value':sub_spec.settings.echogram_min_pixel_value,
                    'echogram_transducer_depth':sub_spec.settings.echogram_transducer_depth,
                    'echogram_delay':sub_spec.settings.echogram_delay,
                    'echogram_temporal_average': sub_spec.settings.echogram_temporal_average,
                    'echogram_stop_at_bottom' : sub_spec.settings.echogram_stop_at_bottom,
                    'echogram_bottom_margin' : sub_spec.settings.echogram_bottom_margin
                   }

        return settings


    def update_echogram_subscription(self, sub_id, pixel_count=500,
            range=100, range_start=0, tvg_function=20, bottom_gain=0,
            tvg_type='sv', bottom_tvg_type='none', echogram_type='surface',
            compression_type='mean', expansion_type='interpolate', echogram_heave=1,
            echogram_ping_filter_state=0, echogram_min_pixel_value=-100,
            echogram_transducer_depth=1, echogram_delay=1, echogram_temporal_average=-1,
            echogram_stop_at_bottom=False, echogram_bottom_margin=0.5):
        '''

        Args:
            sub_id (TYPE):
                DESCRIPTION
            pixel_count (TYPE):
                Optional; DESCRIPTION Defaults to 500.
            range (TYPE):
                Optional; DESCRIPTION Defaults to 100.
            range_start (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            tvg_function (TYPE):
                Optional; DESCRIPTION Defaults to 20.
            bottom_gain (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            tvg_type (TYPE):
                Optional; DESCRIPTION Defaults to 'sv'.
            bottom_tvg_type (TYPE):
                Optional; DESCRIPTION Defaults to 'none'.
            echogram_type (TYPE):
                Optional; DESCRIPTION Defaults to 'surface'.
            compression_type (TYPE):
                Optional; DESCRIPTION Defaults to 'mean'.
            expansion_type (TYPE):
                Optional; DESCRIPTION Defaults to 'interpolate'.
            echogram_heave (TYPE):
                Optional; DESCRIPTION Defaults to 1.
            echogram_ping_filter_state (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            echogram_min_pixel_value (TYPE):
                Optional; DESCRIPTION Defaults to -100.
            echogram_transducer_depth (TYPE):
                Optional; DESCRIPTION Defaults to 1.
            echogram_delay (TYPE):
                Optional; DESCRIPTION Defaults to 1.

        Returns:
            None

        Raises:
            ValueError: Raises ValueError if the subscription id doesn't exist or if
                        the subscription is not a bottom detection subscription.
        '''

        if sub_id not in self.subscriptions:
            raise ValueError('%i is not a valid subscription id' % (sub_id))

        if self.subscriptions[sub_id]['type'] != 'echogram':
            raise ValueError('Error updating echogram subscription. Subscription ' +
                    '%i is not an echogram subscription' % (sub_id))

        #  create a settings object
        sub_settings = ek80_data_client.EchogramSettings()

        #  set the various subscription settings
        sub_settings.pixel_count = pixel_count
        sub_settings.range = range
        sub_settings.range_start = range_start
        sub_settings.tvg_function = tvg_function
        sub_settings.bottom_gain = bottom_gain
        sub_settings.tvg_type = tvg_type
        sub_settings.bottom_tvg_type = bottom_tvg_type
        sub_settings.echogram_type = echogram_type
        sub_settings.compression_type = compression_type
        sub_settings.expansion_type = expansion_type
        sub_settings.echogram_heave = echogram_heave
        sub_settings.echogram_ping_filter_state = echogram_ping_filter_state
        sub_settings.echogram_min_pixel_value = echogram_min_pixel_value
        sub_settings.echogram_transducer_depth = echogram_transducer_depth
        sub_settings.echogram_delay = echogram_delay
        sub_settings.echogram_temporal_average = echogram_temporal_average
        sub_settings.echogram_stop_at_bottom = echogram_stop_at_bottom
        sub_settings.echogram_bottom_margin = echogram_bottom_margin

        #  create an instance of the echogram subs api
        api_instance = ek80_data_client.EchogramSubscriptionsApi(self.data_api_client)

        #  and use it to update our subscription
        api_instance.update_echogram_subscription(sub_id, sub_settings)


    def create_echogram_subscription(self, channel_id, pixel_count=500,
            range=500, range_start=0, tvg_function=20, bottom_gain=0,
            tvg_type='sv', bottom_tvg_type='none', echogram_type='surface',
            compression_type='mean', expansion_type='interpolate', echogram_heave=1,
            echogram_ping_filter_state=0, echogram_min_pixel_value=-100,
            echogram_transducer_depth=1,echogram_delay=1, name=None,
            endpoint_id=None, ek500_db_format=False, echogram_temporal_average=-1,
            echogram_stop_at_bottom=False, echogram_bottom_margin=0.5):
        '''

        Args:
            channel_id (TYPE):
                DESCRIPTION
            pixel_count (TYPE):
                Optional; The number of total  Defaults to 500.
            range (TYPE):
                Optional; DESCRIPTION Defaults to 500.
            range_start (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            tvg_function (TYPE):
                Optional; DESCRIPTION Defaults to 20.
            bottom_gain (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            tvg_type (TYPE):
                Optional; DESCRIPTION Defaults to 'sv'.
            bottom_tvg_type (TYPE):
                Optional; DESCRIPTION Defaults to 'none'.
            echogram_type (TYPE):
                Optional; surface, bottom, or trawl Defaults to 'surface'.
            compression_type (TYPE):
                Optional; mean, peak Defaults to 'mean'.
            expansion_type (TYPE):
                Optional; interpolation, copy Defaults to 'interpolate'.
            echogram_heave (TYPE):
                Optional; DESCRIPTION Defaults to 1.
            echogram_ping_filter_state (TYPE):
                Optional; DESCRIPTION Defaults to 0.
            echogram_min_pixel_value (TYPE):
                Optional; DESCRIPTION Defaults to -100.
            echogram_transducer_depth (TYPE):
                Optional; DESCRIPTION Defaults to 1.
            echogram_delay (TYPE):
                Optional; DESCRIPTION Defaults to 1.
            name (TYPE):
                Optional; DESCRIPTION Defaults to None.
            endpoint_id (TYPE):
                Optional; DESCRIPTION Defaults to None.
            ek500_db_format (BOOL):
                Set to True to return the echogram data in EK500 dB Format.
                See section 3 of the Theory of Operation chapter in the
                EK500 Operator's manual
        Returns:
            The subscription ID as int
        '''

        #  increment the subscription counter
        self.n_subscriptions += 1

        #  if a subscription name is provided, use it, otherwise create one.
        #  The subscription name must be unique.
        if name:
            name = str(name)
        else:
            name = "%i-echogram" % (self.n_subscriptions)

        #  check if we've been provided an endpoint to use. If not, generate one.
        if endpoint_id not in self.endpoints:
            endpoint_id = self.create_server_endpoint()

        #  create an instance of the create subscription API
        api_instance = ek80_data_client.CreateADataSubscriptionApi(self.data_api_client)

        #  create our settings and spec objects
        sub_settings = ek80_data_client.EchogramSettings()

        #  set the various subscription settings
        sub_settings.pixel_count = pixel_count
        sub_settings.range = range
        sub_settings.range_start = range_start
        sub_settings.tvg_function = tvg_function
        sub_settings.bottom_gain = bottom_gain
        sub_settings.tvg_type = tvg_type
        sub_settings.bottom_tvg_type = bottom_tvg_type
        sub_settings.echogram_type = echogram_type
        sub_settings.compression_type = compression_type
        sub_settings.expansion_type = expansion_type
        sub_settings.echogram_heave = echogram_heave
        sub_settings.echogram_ping_filter_state = echogram_ping_filter_state
        sub_settings.echogram_min_pixel_value = echogram_min_pixel_value
        sub_settings.echogram_transducer_depth = echogram_transducer_depth
        sub_settings.echogram_delay = echogram_delay
        sub_settings.echogram_temporal_average = echogram_temporal_average
        sub_settings.echogram_stop_at_bottom = echogram_stop_at_bottom
        sub_settings.echogram_bottom_margin = echogram_bottom_margin

        #  the echogram sub spec requires that the optional init args be specified.
        #  This is different from the bottom subscription. ?
        sub_spec = ek80_data_client.EchogramSubscriptionSpecification(
                channel_id=channel_id, settings=sub_settings,
                subscription_name=name, subscriber_name=self.name)

        #  create the subscription
        sub_id = api_instance.create_echogram_subscription(sub_spec)

        #  add this sub to the subscriptions dict
        self.subscriptions[sub_id] = {'name':name, 'channel_id':channel_id,
                'endpoint_id':endpoint_id, 'type':'echogram',
                'cleanup':self.delete_echogram_subscription,
                'return_db_format':ek500_db_format}

        #  and connect the subscription to the endpoint
        subscription_output_args = ek80_data_client.SubscriptionOutputArgs(sub_id, 'proto-buf')
        api_instance = ek80_data_client.CommunicationEndPointsApi(self.data_api_client)
        api_instance.add_subscription_to_end_point(endpoint_id, subscription_output_args)
        self.endpoints[endpoint_id]['subscriptions'].append(sub_id)

        return sub_id

