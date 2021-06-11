#!/usr/bin/python3
import os, stat_roller, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_player_class, dnd_class, dnd_background, dnd_display, dnd_config_reader
#import os, stat_roller, dnd_features, dnd_language, dnd_tools, dnd_dict, dnd_skills, dnd_race, dnd_player_class, dnd_class, dnd_background, dnd_display

def main():

    dnd_config_reader

# Set initial stats
    stat_roller.stat_selection()

# Choose Race
    dnd_race.player_race()

# Choose Background
    dnd_background.player_background()

# Choose Class
    dnd_player_class.player_class()

# Display the results
    dnd_display.char_display()

if __name__ == '__main__':
    main()
