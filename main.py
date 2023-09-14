import app_frame

try:
    app_frame.app.mainloop()
except ValueError:
    print("Failed to initialize")

if __name__ == "__main__":
    ''' Main loop'''
    app_frame.app.mainloop()
