# IoT-Application-Protocols-for-Smart-Agriculture
Performance Evaluation of IoT Application Protocols for Smart Agriculture
In Smart Agriculture system, Multiple Internet of Things (IoT) protocols are used for data
transmission. Protocols are such as DDS, MQTTSN, SMQTT, CoAP. DDS is an abbreviation
for Data Distribution Service. OMG created this IoT protocol for M2M (Machine to Machine)
 communication (Object Management Group). It provides data interchange via the
 publish-subscribe model. Unlike the MQTT and CoAP protocols, DDS has a 
brokerless architecture. Whereas, CoAP is a common client-server IoT protocol. It enables
 clients to make online transfer requests based on the requirement of the hour.
 However, it also allows supporting servers to reply to incoming queries. To summarize,
 devices' nodes in the IoT ecosystem can only communicate via CoAP. 

Another protocol, SMQTT - Secure Message Queue Telemetry Transport - is more
 secured MQTT protocol.The MQTT protocol is the de-facto standard for IoT messaging.
Standardized by OASIS and ISO, MQTT publish/subscribe protocol provides a
 scalable and reliable way to connect devices over the Internet. Today, MQTT is used
by many companies to connect millions of devices to the Internet. Related to MQTT
 protocol is MQTT-SN. MQTT-SN (MQTT for sensor networks) is an optimized version
 of the MQTT (Message Queuing Telemetry Transport) IoT communications protocol
 built primarily for efficient operation in massive low-power IoT sensor networks.

In comparison with default internet protocol, HTTP - in terms of file size, if we increase the
the volume, then CoAP and DDS stood out from the rest where CoAP performed better.

Whereas, If we increase the client size - then, MQTT-SN, CoAP, SMQTT performed better. 
