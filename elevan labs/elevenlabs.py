import elevenlabs

	
elevenlabs.set_api_key("9995e7dabafe625e6ac1f5f078dbe87c")

voice = elevenlabs.Voice(
    voice_id = "ZQe5CZNOzWyzPSCn5a3c",
    settings = elevenlabs.VoiceSettings(
        stability = 0,
        similarity_boost = 0.75
    )
)
 
audio = elevenlabs.generate(
    text = "Hi, I'm from the future!",
    voice = voice
)
 
elevenlabs.save(audio, "audio.mp3")