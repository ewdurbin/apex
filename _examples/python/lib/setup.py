from setuptools import setup, find_packages

setup(
    name='wu',
    version='0.0.1',
    description='The Wu-Tang Clan is an American hardcore hip hop group from Staten Island, New York City, originally composed of East Coast rappers RZA, GZA, Ol\' Dirty Bastard, Method Man, Raekwon, Ghostface Killah, Inspectah Deck, U-God and Masta Killa.',
    packages=find_packages(where='.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)
