package iotGateway.labs.module7;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapClient;
import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.CoapServer;
import org.eclipse.californium.core.network.Endpoint;

public class CoapServerConnector {
	private static final Logger _Logger = 
			Logger.getLogger(CoapServerConnector.class.getName());
	
	private CoapServer _coapServer;
	private String _protocol;
	private String _host;
	private int _port;
	private CoapClient _clientConn;
	private String _serverAddr;
	public CoapServerConnector() {
		this("localhost");
	}
	
	public CoapServerConnector(String host) {
		super();
		
		_protocol = "coap";
		_port = 5683;
		
		if (host != null && host.trim().length() > 0) {
			_host = host;

		} else {
			_host = "localhost";

		}

		
		
		System.out.println("in coap constructor");
		_coapServer = new CoapServer();
		
		TempResourceHandler resourceTemp = new TempResourceHandler("temp");
		addResource(resourceTemp);
	}
	
	public void addDefaultResource(String Name) {
		
	}
	public void addResource(CoapResource resource) {
		if (resource != null) {
			if (_coapServer != null) {
				
				_coapServer.add(resource);
			}
		}
	}
	public void start() {
		System.out.println("in coap start");
		if (_coapServer == null) {
			System.out.println("in coap, coapserver is null");

			_Logger.info("Creating CoAP server instance and 'temp' handler...");
			_coapServer = new CoapServer();
			TempResourceHandler tempHandler = new TempResourceHandler("temp");
			_coapServer.add(tempHandler);
		}
		_Logger.info("Starting CoAP server...");
		_coapServer.start();
		System.out.println("coap endpoint :  ---" + _coapServer.getEndpoint(5683).getAddress());
	}
	
	public void stop() {
		_coapServer.stop();
	}


}
