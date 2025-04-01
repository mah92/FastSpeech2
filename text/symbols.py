"""Simplified symbol system with explicit initialization"""
from pathlib import Path

_symbols = None
_symbol_to_id = None
_id_to_symbol = None

def initialize(tokens_path):
    global _symbols, _symbol_to_id, _id_to_symbol
    path = Path(tokens_path)
    
    # Handle case where path is directory (old behavior)
    if path.is_dir():
        path = path / "tokens.txt"
    
    if not path.exists():
        raise FileNotFoundError(f"Tokens file not found at {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        _symbols = [line.split()[0] for line in f if line.strip()]
    
    _symbol_to_id = {s: i for i, s in enumerate(_symbols)}
    _id_to_symbol = {i: s for i, s in enumerate(_symbols)}

def get_symbols():
    if _symbols is None:
        raise RuntimeError("Symbols not initialized. Call initialize() first")
    return _symbols

def get_symbol_to_id():
    if _symbol_to_id is None:
        raise RuntimeError("Symbols not initialized. Call initialize() first")
    return _symbol_to_id

def get_id_to_symbol():
    if _id_to_symbol is None:
        raise RuntimeError("Symbols not initialized. Call initialize() first")
    return _id_to_symbol

def text_to_sequence(text, cleaner_names):
    return [get_symbol_to_id().get(s, get_symbol_to_id()["?"]) for s in text]

def sequence_to_text(sequence):
    return ''.join([get_id_to_symbol().get(i, "?") for i in sequence])

# Special symbols
PAD = "_"
UNK = "?"
BOS = "^"
EOS = "$"

@property
def PAD_ID():
    return 0

@property 
def UNK_ID():
    return get_symbol_to_id().get(UNK, 1) if _symbol_to_id is not None else 1

@property
def BOS_ID():
    return get_symbol_to_id().get(BOS, 2) if _symbol_to_id is not None else 2

@property
def EOS_ID():
    return get_symbol_to_id().get(EOS, 3) if _symbol_to_id is not None else 3
