from ovos_plugin_manager.g2p import Grapheme2PhonemePlugin
from distutils.spawn import find_executable
from ovos_utils.lang.phonemes import ipa2arpabet
import subprocess


class EspeakPhonemesPlugin(Grapheme2PhonemePlugin):

    def __init__(self, config=None):
        super().__init__(config)
        self.espeak_bin = find_executable("espeak-ng")  or \
                         find_executable("espeak") or \
                         "espeak"

    def get_espeak_phonemes(self, sentence, lang):
        args = [self.espeak_bin, '-q', '-x', '--ipa', '-v', lang, sentence]
        phonemes = []
        for pho in subprocess.check_output(args).decode("utf-8").\
                replace(" ", "ˈ").replace("ː", "ˈ").replace('̃', "").strip().split("ˈ"):
            if pho in ipa2arpabet:
                phonemes.append(pho)
            else:
                phonemes += list(pho)
        return phonemes

    def get_ipa(self, word, lang):
        return self.get_espeak_phonemes(word, lang)

