
set executable=.\swagger-codegen-cli-3.0.71.jar

java -Xmx1024M -jar "%executable%" generate -i ".\EK80_data_server_26.2.json" -l python -o ".\ek80dataclient" -c "ek80_data_config.json"