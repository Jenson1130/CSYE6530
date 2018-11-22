package iotGateway.labs.module7;

import java.util.logging.Logger;
import java.util.logging.Level;

public class CoapClientTestApp {
	private static final Logger _Logger = 
			Logger.getLogger(CoapClientTestApp.class.getName());
	
	private static CoapClientTestApp _App = null;
	
	public CoapClientTestApp() {
		super();
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		try {
			_App = new CoapClientTestApp();
			_App.start();
		} catch (Exception e) {
			_Logger.log(Level.SEVERE, "Bad staff ", e);
			e.printStackTrace();
			System.exit(1);
		}

	}
	
	public void start() {
		CoapClientConnector clientConn = new CoapClientConnector();
		clientConn.runTests("temp");
		clientConn.sendGetRequest();
		
	}


}
