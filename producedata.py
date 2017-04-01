from kafka import KafkaProducer
import login as pbbuf
import time
import fsp_proto_pb2 as fsp_pb
producer=KafkaProducer(bootstrap_servers='192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092')
# cpbuf=pbbuf.ClientConnected(87,"ablert_test")
# producer.send('ablert_test',cpbuf)



#here , the topic is for consumer
for i in range(401,445):
    cpbuf=pbbuf.ClientConnected(i)
    producer.send('albert_test',cpbuf)
    time.sleep(1)
    # cpt = fsp_pb.ClientConnected()
    # cpt.ParseFromString(cpbuf[5])
    # print cpt.client_id
    # print cpt.app_id
    # print cpt.client_name

    print i
