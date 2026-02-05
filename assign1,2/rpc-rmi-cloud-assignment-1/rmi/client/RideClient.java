package client;

import common.RideService;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RideClient {

    public static void main(String[] args) {
        try {
            // 👇 PUBLIC IP of your EC2 instance
            String serverIP = "3.110.167.208";

            Registry registry = LocateRegistry.getRegistry(serverIP, 1099);

            RideService service =
                    (RideService) registry.lookup("RideService");

            System.out.println("✅ Connected to RMI Server");

            System.out.println("Fare: " +
                    service.calculateFare(10, 20));
            System.out.println("Driver: " +
                    service.assignDriver("Perungudi"));
            System.out.println("ETA: " +
                    service.estimateETA(10));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
