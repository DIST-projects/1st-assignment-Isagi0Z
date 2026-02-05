package common;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RideService extends Remote {
    double calculateFare(int distanceKm, int timeMinutes) throws RemoteException;
    String assignDriver(String location) throws RemoteException;
    int estimateETA(int distanceKm) throws RemoteException;
}
