"""Text cleaners for IPA input only"""

import re

# Regular expression matching whitespace
_whitespace_re = re.compile(r'\s+')

def collapse_whitespace(text):
    """Normalize all whitespace to single spaces"""
    return re.sub(_whitespace_re, ' ', text).strip()

def ipa_cleaners(text):
    """Primary cleaner for IPA text input
    
    Args:
        text: Input text in IPA format
    
    Returns:
        Cleaned IPA text with:
        - Normalized whitespace
        - Invalid characters removed
        - Proper IPA formatting
    """
    # Remove any characters not in our IPA symbol set
    # Note: This should match the symbols in your tokens_sherpa_with_fa.txt
    text = re.sub(
        r'[^\wˈˌːˑ ̩‿.?!, \-a-zA-Z'  # Base IPA and punctuation
        r'æçðøħŋœǀǁǂɐɑɒɓɔɕɖɗɘəɚɛɜɞɟɠɡɢɣɤɥɦɧɨɪɫɬɭɮɯɰɱɲɳɴɵɶɸɹɺɻɽɾʀʁʂʃʄʈʉʊʋʌʍʎʏʐʑʒʔʕʘʙʛʜʝʟʡʢ'  # IPA extensions
        r'βθχᵻⱱ'  # Additional phonetic symbols
        r']', 
        '', 
        text
    )
    
    # Normalize whitespace and strip
    text = collapse_whitespace(text)
    
    return text

# For backward compatibility with FastSpeech2 code
basic_cleaners = ipa_cleaners