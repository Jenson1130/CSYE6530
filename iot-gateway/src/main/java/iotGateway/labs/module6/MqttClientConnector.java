package iotGateway.labs.module6;

import java.util.logging.Level;
import java.util.logging.Logger;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttClientConnector implements MqttCallback {
	
		private static final Logger _Logger = Logger.getLogger(MqttClientConnector.class.getName());

		private String _protocol; 
		private String _host;
		private int _port; 
		private String _clientID;
		private String _brokerAddr;
		private MqttClient _mqttClient;

		/**
		 * Default.
		 *
		 */
		/**
		 * Constructor.
		 *
		 * @param host     The name of the broker to connect.
		 * @param isSecure Currently unused.
		 */
		public MqttClientConnector(String host, String protocol, int port) {
			super();
	
			if (host != null && host.trim().length() > 0) {
				_host = host;
				_protocol = protocol;
				_port = port;
				
			}

			_clientID = MqttClient.generateClientId();
			_Logger.info("Client ID: " + _clientID);
			_brokerAddr = _protocol + "://" + _host + ":" + _port;
			_Logger.info("Broker's URL: " + _brokerAddr);
		}

		public void connect()
	    {
	        if (_mqttClient == null) {
	       
	              MemoryPersistence persistence = new MemoryPersistence();
	              try {
	                     _mqttClient = new MqttClient(_brokerAddr, _clientID, persistence);
	                     MqttConnectOptions connOpts = new MqttConnectOptions();
	                     connOpts.setCleanSession(true);
	                     _mqttClient.setCallback(this);
	                     _mqttClient.connect(connOpts);
	                     _Logger.info("Connected to broker: " + _brokerAddr);
	                     
	                     
	                    
	              } catch (MqttException e) {
	              _Logger.log(Level.SEVERE, "Unable to connect to broker.");
	              }
	        }
	    }

		public void disconnect() {
			try {
				_mqttClient.disconnect();
				_Logger.info("Disconnected from broker: " + _brokerAddr);
			} catch (Exception e) {
				_Logger.log(Level.SEVERE, "Failed to disconnect from broker: " + _brokerAddr, e);
			}
		}

		/**
		 * Publishes the given payload to broker directly to topic 'topic'.
		 *
		 * @param topic
		 * @param qosLevel
		 * @param payload
		 */
		public boolean publishMessage(String topic, int qosLevel, byte[] payload) {
			boolean success = false;
			try {
				_Logger.info("Topic: " + topic);
				MqttMessage msg = new MqttMessage(payload);
				msg.setQos(qosLevel);
				msg.setRetained(true);
				_mqttClient.publish(topic, msg);
				
				success = true;
			} catch (Exception e) {
				_Logger.log(Level.SEVERE, "Failed to publish MQTT: " + e.getMessage());
			}
			return success;
		}

		public boolean subscribeToAll() {
			try {
				
				_mqttClient.subscribe("$SYS/#");
				_Logger.log(Level.INFO, "Successful!");
				return true;
			} catch (MqttException e) {
				_Logger.log(Level.WARNING, "Failed to subscribe to all topics.", e);
			}
			return false;
		}

		public boolean subscribeToTopic(String topic) {
			try {
				_mqttClient.subscribe(topic);
				System.out.println("subscribe successful!");
				return true;
			} catch (MqttException e) {
				e.printStackTrace();
			}
			return false;
		}

		/*
		 * (non-Javadoc)
		 *
		 * @see org.eclipse.paho.client.mqttv3.MqttCallback#connectionLost(java.lang.
		 * Throwable)
		 */
		public void connectionLost(Throwable t) {
			_Logger.log(Level.WARNING, "Connection failed!", t);
		}

		/*
		 * (non-Javadoc)
		 *
		 * @see
		 * org.eclipse.paho.client.mqttv3.MqttCallback#deliveryComplete(org.eclipse.paho
		 * .client.mqttv3.IMqttDeliveryToken)
		 */
		public void deliveryComplete(IMqttDeliveryToken token) {
			try {

				_Logger.info("Delivery complete: " + token.getMessageId() + " - " + token.getResponse() + " - "
						+ token.getMessage());
			} catch (Exception e) {
				_Logger.log(Level.SEVERE, "Failed to retrieve message.", e);
			}
		}

		/*
		 * (non-Javadoc)
		 *
		 * @see
		 * org.eclipse.paho.client.mqttv3.MqttCallback#messageArrived(java.lang.String,
		 * org.eclipse.paho.client.mqttv3.MqttMessage)
		 */
		public void messageArrived(String data, MqttMessage msg) throws Exception {
			_Logger.info("Message arrived: " + data + ", " + msg.getId() + ", " + msg.toString());
		}



}
