from neon_g2p_espeak_plugin import EspeakPhonemesPlugin

print(EspeakPhonemesPlugin().get_arpa("hello", "en"))
print(EspeakPhonemesPlugin().get_ipa("João", "pt"))
print(EspeakPhonemesPlugin().utterance2arpa("hello world", "en"))
print(EspeakPhonemesPlugin().utterance2visemes("hello world", "en"))
