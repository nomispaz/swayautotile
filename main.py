from i3ipc import Connection, Event

def main():
    # Create the Connection object that can be used to send commands and subscribe
    # to events.
    i3 = Connection()
    
    # Get the name of the focused window
    focused = i3.get_tree().find_focused()
    print('Focused window %s is on workspace %s' %
          (focused.name, focused.workspace().name))
    
    # set layout(split horizontalor vertical according to geometry of current window)
    if focused.rect.height > focused.rect.width:
        new_layout = "splitv"
    else:
        new_layout = "splith"
        
    # Send the new command to be executed synchronously.
    i3.command(new_layout)
        
    # Start the main loop and wait for events to come in.
    i3.main()

if __name__ == "__main__":
    main()
