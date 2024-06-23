from os import environ
import json

from kafka import KafkaConsumer
from pathlib import Path
from playsound import playsound

kafka_hostname = environ.get('KAFKA_HOSTNAME', 'localhost')
kafka_port = environ.get('KAFKA_PORT', '9092')
kafka_topic = environ.get('KAFKA_TOPIC', 'ctfmanager')

consumer = KafkaConsumer(bootstrap_servers=f'{kafka_hostname}:{kafka_port}',
                         auto_offset_reset='latest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

consumer.subscribe([kafka_topic])
print(f"\n🚀 J'ai souscrit au topic « {kafka_topic} » sur le serveur Kafka à l'adresse {kafka_hostname}:{kafka_port}.\n")

audio_directory = Path(__file__).parent / "audio"

for message in consumer:
    tags = message.value.get('tags')

    print(f"Message : {message.value}")
    print(f"Tags : {tags}")

    if tags:
        search = "sound_"
        for tag in tags:
            if tag.startswith(search):
                print(f"Tag {tag} trouvé")

                # Extraire le nom du fichier à partir du tag
                sound_file_name = tag[len(search):] + ".mp3"

                sound_file_path = audio_directory / sound_file_name
                print(f"🎵 Lecture du fichier audio : {sound_file_path}\n")

                if sound_file_path.is_file():
                    try:
                        playsound(str(sound_file_path))
                    except Exception as e:
                        print(f"Erreur lors de la lecture du fichier audio {sound_file_path}: {e}\n")
                else:
                    print(f"Le fichier audio {sound_file_path} n'existe pas.\n")
