import subprocess
from distutils.spawn import find_executable

from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
from ovos_utils.lang.phonemes import ipa2arpabet


class EspeakPhonemesPlugin(Grapheme2PhonemePlugin):

    def __init__(self, config=None):
        super().__init__(config)
        self.espeak_bin = find_executable("espeak-ng") or \
                          find_executable("espeak") or \
                          "espeak"

    def get_espeak_phonemes(self, sentence, lang):
        args = [self.espeak_bin, '-q', '-x', '--ipa', '-v', lang, sentence]
        phonemes = []
        for pho in subprocess.check_output(args).decode("utf-8"). \
                replace(" ", "ˈ").replace("ː", "ˈ").replace('̃', "").strip().split("ˈ"):
            if pho in ipa2arpabet:
                phonemes.append(pho)
            else:
                phonemes += list(pho)
        return phonemes

    def get_ipa(self, word, lang, ignore_oov=False):
        return self.get_espeak_phonemes(word, lang)

    @staticmethod
    def get_languages():
        a = subprocess.check_output("espeak --voices".split()).decode("utf-8")
        for l in a.split("\n")[1:]:
            print(l.split())
        return [(l.split()[1], l.split()[3]) for l in a.split("\n")[1:] if l]

    @property
    def available_languages(self):
        """Return languages supported by this G2P implementation in this state
        This property should be overridden by the derived class to advertise
        what languages that engine supports.
        Returns:
            set: supported languages
        """
        return set([l[0] for l in self.get_languages()])


# sample valid configurations per language
# "display_name" and "offline" provide metadata for UI
# "priority" is used to calculate position in selection dropdown
#       0 - top, 100-bottom
# all keys represent an example valid config for the plugin
EspeakG2PConfig = {
    l: [
        {"lang": l,
         "display_name": f"Espeak G2P ({r})",
         "priority": 60,
         "native_alphabet": "IPA",
         "durations": False,
         "offline": True}
    ] for l, r in EspeakPhonemesPlugin.get_languages()
} if find_executable("espeak-ng") or find_executable("espeak") else {}

if __name__ == "__main__":
    from pprint import pprint

    pprint(EspeakG2PConfig)
