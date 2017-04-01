# KafkaProducer
本项目是一个kafka生产者，主要用来生产消息，然后发送往kafka集群中。


producer=KafkaProducer(bootstrap_servers='192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092')这句话 表示kafka集群 的地址是192.168.7.60:9092,192.168.7.61:9092,192.168.7.62:9092， producer就是获取了一个生产者。

cpbuf=pbbuf.ClientConnected(i) 表示 返回一个PB格式 消息
