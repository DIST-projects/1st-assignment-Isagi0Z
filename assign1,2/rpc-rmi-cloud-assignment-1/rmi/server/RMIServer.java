package server;

import common.RideService;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "3.110.167.208");

            RideService service = new RideServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("RideService", service);

            System.out.println("✅ RMI Server running...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}