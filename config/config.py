class Config:
    
    # general window properties
    window_height = 800
    window_width = 1200

    # properties of the instructions
    instructions_bg_color = "white"
    instructions_font_color = "black"
    instructions_font_size = 18
    instructions_font = "helvetica"
    instruction_delay = 1000  # amount of time that timed instructions are on the screen

    # properties of the text and image stimuli
    stimulus_bg_color = "white"
    stimulus_font_color = "black"
    stimulus_font_size = 32
    stimulus_font = "helvetica"
    image_stimulus_height = 400
    image_stimulus_width = 400
    inter_trial_interval = 1000  # amount of time between trials, in ms
    stimulus_presentation_time = 1000  # amount of time each word or image is on the screen
    
    num_familiarization_trials = 30
    familiarization_key_list = None

    num_test_trials = 30
    test_from_fam_proportion = 0.5
    test_delay = 1000

    condition = 1
    instruction_file_path = "stimuli/word_instructions.txt"
    
    stimulus_type_list = "words"




    SHAPES = ["circle", "triangle", "square", "rectangle", "hexagon"]

    WORDS = ["banana", "quarter", "apple", "car", "child", "college", "illinois"]

    # dictionary to store shapes and paths to display in recognition task
    SHAPE_PATHS = {
        "triangle": "shapes/triangle.jpg",
        "rectangle": "rectangle/rectangle.jpg",
        "square": "square/square.jpg",
        "hexagon": "hexagon/hexagon.jpg",
        "circle": "circle/circle.jpg",
        "oval": "oval/oval.jpg",
        "rhombus": "rhombus/rhombus.jpg"
    }
    
    ######