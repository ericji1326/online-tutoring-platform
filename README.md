# Inspiration
We were inspired to create this tutoring platform due to our own experiences with online schooling during the COVID-19 pandemic. We recognized the demand for such platforms and learned firsthand that while online schooling may save time, money and be more convenient, it comes with it's own set of challenges as well. As machine learning enthusiasts, we were determined to tackle these issues with AI.

# What it does
LevelUp allows two-way video and audio communication between the tutor and one or more students when they join a classroom. If the user's role is assigned as Tutor, the application will capture image sequences from the student's videostream and make a GET request to our backend API. This API preprocesses the images and feeds them through a facial expression recognition machine learning model that is pre-loaded. The model will interpret the students' expressions and return a prediction, which is displayed to the tutor on the front-end. This enables the tutor to understand the students' response during a session and better cater to their learning needs.

# How we built it
Our web application was built with React and the Twilio API. The facial expression recognition machine learning model was deployed in the back-end using Flask. This model was pre-trained on the FER2013 dataset by engineering students at Boston university. More information on this model's development is available at this link: https://arxiv.org/ftp/arxiv/papers/2105/2105.03588.pdf. To pass image data to the back-end API, we utilized the Firebase cloud platform to store Base64 encodings of the images, which were then decoded in our flask API.

# Challenges we ran into
We ran into difficulties when determining how to pass image data to our API. The Base64 encodings were tens of thousands of characters in length and could not be passed as a typical HTTP GET request query string. We eventually decided upon using Firebase to store and retrieve Base64 encodings. We also faced challenges in streamlining the process of making predictions with our ML model such that the tutor would receive student expression data with minimal latency.

# Accomplishments that we're proud of
Through this project, we learned a lot about creating an end-to-end application. We were especially excited when we successfully productionized our pretrained machine learning model to interface with our React application through a Web API.

# What's next for LevelUp Tutoring
During this hackathon, we successfully created another machine learning model using image segmentation techniques that could identify objects in the student's videostream. This could be used to determine if the student is distracted (ie. if the model detects the student is using their phone). A further expansion of this tutoring platform could involve an online examination mode which can use object detection and/or eye-tracking to proctor students for signs of cheating.

# Additional Resources
The backend files and ML models used in this project were too large to be posted on this repository. They can be accessed here: https://mcgill-my.sharepoint.com/:u:/g/personal/mingyang_li_mail_mcgill_ca/EQrptgGaxk9Dh28Q_wfhs_QBLV3w5C2mj2OIslAnvNBpPw?e=B183Zx
