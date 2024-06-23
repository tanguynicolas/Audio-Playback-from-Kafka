# Audio-Playback-from-Kafka

Read audio file (mp3) from specific tag in specific JSON document format, published in Kafka topic. Used as part of CTF Manager.

Format is `{ "tags": ["sound_*"] }`. Tagg must start by `sound_`. The rest of the string must match MP3 file name, present in `audio/` directory.

See example [here](#produce-to-trigger).

## Configuration

Set environment variable.

| Variable       | Default          |
| -------------- | ---------------- |
| KAFKA_HOSTNAME | localhost (str)  |
| KAFKA_PORT     | 9092 (str)       |
| KAFKA_TOPIC    | ctfmanager (str) |

## Start

### Without Docker

Install dependancies.

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then start.

```shell
python main.py
```

### With Docker

```shell
docker run --rm -e "KAFKA_HOSTNAME=${KAFKA_HOSTNAME}" \
    -e "KAFKA_PORT=${KAFKA_PORT}" \
    tanguynicolas/audio-playback-from-kafka
```

## Manually produce

To trigger sound playback manually.

### Install Kafka

1. Download the [latest Kafka](https://www.apache.org/dyn/closer.cgi?path=/kafka/3.7.0/kafka_2.13-3.7.0.tgz#http) version.
2. Execute these commands (adapt):

```shell
tar -xzf kafka_2.13-3.7.0.tgz
rm kafka_2.13-3.7.0.tgz
sudo mv kafka_2.13-3.7.0 /opt/kafka
chown "$USER:$USER" -R /opt/kafka
```

3. Add /opt/kafka/bin to your `PATH`.

### Produce to trigger

```shell
echo '{ "tags": ["sound_machine_gun"] }' | kafka-console-producer.sh --bootstrap-server "${KAFKA_HOSTNAME}:${KAFKA_PORT}" --topic "${KAFKA_TOPIC}"
```
