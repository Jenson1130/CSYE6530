package iotGateway.labs.module7;

import java.util.logging.Logger;
import java.util.logging.Level;

public class CoapServerTestApp {
	private static final Logger _Logger = 
			Logger.getLogger(CoapServerTestApp.class.getName());
	
	private static CoapServerTestApp _App = null;
	
	public CoapServerTestApp() {
		super();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			_App = new CoapServerTestApp();
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.SEVERE, "Bad staff ", e);
			System.exit(1);
		}

	}

	
	public void start() {
		System.out.println("in app start");
		CoapServerConnector serverConn = new CoapServerConnector();
		serverConn.start();
		
	}


}
