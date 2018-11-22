package iotGateway.labs.module7;

import java.util.logging.Logger;

import org.eclipse.californium.core.CoapResource;
import org.eclipse.californium.core.coap.CoAP.ResponseCode;
import org.eclipse.californium.core.server.resources.CoapExchange;


public class TempResourceHandler extends CoapResource{
	//static
		private static final Logger _Logger = 
				Logger.getLogger(TempResourceHandler.class.getName());
		
		//constructors
		
		public TempResourceHandler() {
			super("default");
		}

		/**
		 * @param name
		 */
		public TempResourceHandler(String name) {
			super(name);
			System.out.println("in temp constructor");
		}

		/**
		 * @param name
		 * @param visible
		 */
		public TempResourceHandler(String name, boolean visible) {
			super(name, visible);
		}
		
		
		@Override
		public void handleGET(CoapExchange ce) {
			
			String responseMsg =  "here is my response to:" + super.getName();

			ce.respond(ResponseCode.VALID, responseMsg);
			
			_Logger.info("Handling GET:" + responseMsg);
			_Logger.info(ce.getRequestCode().toString() + ": " + ce.getRequestText());
		}
		
		@Override
		public void handlePOST(CoapExchange exchange) {
			String responseMsg =  "Response to:" + super.getName();

			System.out.println(exchange.getRequestText());
			exchange.respond(ResponseCode.VALID, responseMsg);
			
			_Logger.info("Handling POST:" + responseMsg);
			_Logger.info(exchange.getRequestCode().toString() + ": " + exchange.getRequestText());
		}
		
		@Override
		public void handlePUT(CoapExchange exchange) {
			String responseMsg =  "here is my response to:" + super.getName();
			
			exchange.respond(ResponseCode.VALID, responseMsg);
			
			_Logger.info("Handling PUT:" + responseMsg);
			_Logger.info(exchange.getRequestCode().toString() + ": " + exchange.getRequestText());
		}
		
		@Override
		public void handleDELETE(CoapExchange exchange) {
			String responseMsg =  "Response to:" + super.getName();
			
			exchange.respond(ResponseCode.VALID, responseMsg);
			
			_Logger.info("Handling DELETE:" + responseMsg);
			_Logger.info(exchange.getRequestCode().toString() + ": " + exchange.getRequestText());
		}


}
