from neon_g2p_espeak_plugin import EspeakPhonemesPlugin



print(EspeakPhonemesPlugin().utterance2arpa("hello world", "en"))
print(EspeakPhonemesPlugin().utterance2visemes("hello world"))

print(EspeakPhonemesPlugin().get_ipa("João", "pt"))