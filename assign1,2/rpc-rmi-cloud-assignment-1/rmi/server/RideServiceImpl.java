package server;

import common.RideService;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class RideServiceImpl extends UnicastRemoteObject implements RideService {

    public RideServiceImpl() throws RemoteException {
        super(5000); // 🔥 FIXED PORT
    }

    public double calculateFare(int distanceKm, int timeMinutes) {
        return 50 + distanceKm * 12 + timeMinutes * 2;
    }

    public String assignDriver(String location) {
        String[] drivers = {"Arun", "Suresh", "Ravi"};
        return drivers[Math.abs(location.hashCode()) % drivers.length];
    }

    public int estimateETA(int distanceKm) {
        return (distanceKm * 60) / 40;
    }
}    