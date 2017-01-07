package com.ubclasergriffins.openobd.devices;

/**
 * Created by kaiboma on 2017-01-06.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DeviceManager {

    /**
     * A map of sample (dummy) items, by ID.
     */
    public static final List<Devices> DEVICES_LIST = new ArrayList<Devices>();

    public static final Map<String, Devices> DEVICES_MAP = new HashMap<String, Devices>();

    private static final String[] DEVICES = {"GPS", "OBD", "ACCEL", "THERMO"};

    static {
        // Add some sample items.
        for (int i = 0; i < DEVICES.length; i++) {
            addItem(createDeviceItem(DEVICES[i]));
        }
    }

    private static void addItem(Devices item) {
        DEVICES_LIST.add(item);
        DEVICES_MAP.put(item.id, item);
    }

    private static Devices createDeviceItem(String device) {
        return new Devices(device, "Item " + device, makeDetails(device));
    }

    private static String makeDetails(String device) {
        StringBuilder builder = new StringBuilder();
        builder.append("Details about ").append(device);
        builder.append("\nMore details information here.");
        if(device == "GPS"){
            builder.append("\n GPS");
        }
        else if(device == "OBD"){
            builder.append("\n OBD");
        }
        else if(device == "THERMO"){
            builder.append("\n THERMO");
        }
        else if(device == "ACCEL") {
            builder.append("\n ACCEL");
        }

        return builder.toString();
    }

    /**
     * A dummy item representing a piece of content.
     */
    public static class Devices {
        public final String id;
        public final String content;
        public final String details;

        public Devices(String id, String content, String details) {
            this.id = id;
            this.content = content;
            this.details = details;
        }

        @Override
        public String toString() {
            return content;
        }
    }
}

