Conceptual Overview of DRAGG
============================

The GNOMES competition is built on the Distributed Resource AGGregator (DRAGG) simulation engine. DRAGG combines common household resources such as electric HVAC equipment (e.g. heat pumps), electric resistance water heaters, electric vehicles, photovoltaic (“PV”) generation, and home batteries to determine the aggregate load profile for a community of homes. For GNOMES you will only be responsible for the HVAC, water heater, and electric vehicle.

At each timestep environmental conditions such as outdoor air temperature (OAT), solar irradiance (GHI), and uncontrollable hot water use will impact the indoor air temperature and hot water tank temperature. Additionally the electric vehicle will be used throughout the day. Just as in a physical house, the virtual representation in DRAGG controls each of these resources to ensure the house is comfortable to the greatest degree possible: the HVAC will kick on when the house is too warm, and the water heater will turn on if the hot water goes cold. 

However, as described in “Welcome to GNOMES4Homes” some times of day are more convenient for running these appliances than others.

You can control your home's resources and get rewarded by the GNOMES utility for doing so! You may control your appliances in the following ways:

1.	The HVAC setpoints may be changed throughout the day. Please note that your HVAC is not guaranteed to respond to the change in setpoint because the temperature “floats” -- HVAC controls operate with a deadband to reduce the number of times the HVAC turns on and off. (“Cycling” behavior where the equipment turns on and off frequently can damage motors.) This is also why there is a minimum time duration for all your inputs. To ensure control of your HVAC that is reasonable, your setpoints will only be allowed to be between X and Y. 
2.	The water heater may be cycled on/off with direct control. Because electric resistance water heaters operate by running electric current through a conductor there is little risk to physical damage by cycling the water heater. To ensure safety your hot water must maintain a minimum temperature of X (to kill bacteria) and a maximum temperature of Y (to avoid scalding occupants).
3.	The electric vehicle charge is directly controllable at times when the electric vehicle is parked at home and not about to leave. The electric storage provided by the vehicle can offset some of the demand throughout the day to reduce peak loads.

