import json
from kafka import KafkaProducer


class KafkaMsgProducer:
    def __init__(self, server):
        self._server = server
        self.producer = None

    def connect(self):
        if self.producer is None:
            producer = KafkaProducer(bootstrap_servers=self._server)
            self.producer = producer

    def close(self):
        if self.producer is not None:
            self.producer.close()
            self.producer = None

    def send(self, topic, msg):
        if self.producer is not None:
            if not isinstance(msg, bytes):
                msg = msg.encode("utf-8")  # 将str类型转换为bytes类型
            self.producer.send(topic=topic, value=msg)


def run():
    print("Start sending msg to kafka!")

    msg = {
        "dfpFlows":
            [
                {
                    "passiveIP": "[, 192.168.90.210, 122.122.1.4, ]",
                    "outCode": "BNrKy7_PJoGtkg9XB1AoLTQDeI46kfoWZAc0NfIi5b8Dugx3g65JKMAOxBXLOyg0MH3l8_k_zjDfCRYZlTHsvopPJR7gKk2f5kAxR7D952ZjS-YPp953ZL2-NR5c2OdkI4pdpHPY8j-prwLm-m4Gd7rrXHUGvCLIplAn4y6-DT4yHKGsGRaqq3rhW3lcwTu_Q41k_7LdrvjGmxWP7CVlYbi6VajFZxExkfRINA_llnJx-vhq",
                    "match":
                        {
                            "cookieCode": 10000
                        },
                    "startupTime": "1519625508",
                    "IMEI": "357523056499288",
                    "updateTime": 1627895830394,
                    "platform": "AND",
                    "wifiMacAddress": "d0:22:be:e6:97:11",
                    "dfp": "MACUBjG0nGtk45soH_5I7aKwTDm-GPKW",
                    "bluetooth": "c4:62:ea:bb:ea:f9",
                    "passiveCode": "mM8-dmH08YDzWJelbhpTo9xOvYyRGPjz",
                    "createTime": 1627895830394,
                    "crc64Code": "-7351107397746447091",
                    "IMSI": "460013650022151",
                    "custID": "123",
                    "localCode": "192.168.90.210",
                    "cookieCode": "EAD4QMhM3hHwSvfjTWhcOgVEBn-HG_dA",
                    "androidID": "NHCGIqBp7pIOHi5Cnl2RFZPFPldo5gdn",
                    "wifiListHash": "7a00af92dc189572",
                    "possbility": 10000,
                    "timestamp": "1608106008101"
                }
            ]
    }

    print(json.dumps(msg))

    msg = {"field":"localCode","dataType":"dfp_element_ratio_top","custID":"all","type":"TOP100","value":1.0000,"platform":"WEB","timestamp":1628783999000}

    producer = KafkaMsgProducer("10.100.1.72:9092")
    producer.connect()  # 建立连接
    # topic = "dfp-logstash"
    topic = "dfp-statistics"

    producer.send(topic=topic, msg=json.dumps(msg))


if __name__ == '__main__':
    run()  # 运行发布消息程序
