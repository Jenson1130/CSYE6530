package iotGateway.labs.module6;

import java.util.logging.Logger;

public class MqttSubClientTestApp {
    private static final Logger _Logger = Logger.getLogger(MqttSubClientTestApp.class.getName());
    private static MqttSubClientTestApp _App;
    /**
     * @param args
     */
    public static void main(String[] args)
    {
       _App = new MqttSubClientTestApp();
       try {
              _App.start();
       } catch (Exception e) {
              e.printStackTrace();
       } 
    }
    private MqttClientConnector _mqttClient;
    /**
     * Default.
     */
    public MqttSubClientTestApp()
    {
    	super(); 
    	}
    /**
     * Connect to the MQTT client, then:
     * 1) If this is the subscribe app, subscribe to the given topic
     * 2) If this is the publish app, publish a test message to the given topic
     */
    public void start()
    {
        _mqttClient = new MqttClientConnector("test.mosquitto.org","tcp",1883);
        _mqttClient.connect();
        String topicName = "test";
        _mqttClient.subscribeToTopic(topicName);

    }
}



