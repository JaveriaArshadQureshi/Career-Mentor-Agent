from agents import function_tool

@function_tool
def get_career_roadmap(field : str) -> str :
    maps = {
        "software_engineering": "1. Learn programming languages (Python, Java, etc.)\n2. Master data structures and algorithms\n3. Build projects to showcase skills\n4. Contribute to open source\n5. Apply for internships\n6. Network with professionals in the field\n7. Prepare for technical interviews",
        "data_science": "1. Learn statistics and mathematics\n2. Master data manipulation",
        "machine_learning" : "1. Understand machine learning algorithms\n2. Learn Python libraries (NumPy, Pandas, Scikit-learn)\n3. Work on real-world datasets\n4. Participate in Kaggle competitions\n5. Build a portfolio of projects\n6. Stay updated with the latest research",
        "web_development": "1. Learn HTML, CSS, and JavaScript\n2. Master front-end frameworks (React, Angular, etc.)\n3. Learn back-end technologies (Node.js, Django, etc.)\n4. Build full-stack applications\n5. Understand web security best practices\n6. Deploy applications on cloud platforms",
        "cybersecurity": "1. Learn networking fundamentals\n2. Understand operating systems and security protocols\n3. Master penetration testing tools\n4. Get certified (CompTIA Security+, CEH, etc.)\n5. Participate in Capture The Flag (CTF) competitions\n6. Stay updated with the latest security threats and trends",
        "cloud_computing": "1. Understand cloud service models (IaaS, PaaS, SaaS)\n2. Learn about major cloud providers (AWS, Azure, GCP)\n3. Master cloud deployment and management tools\n4. Get certified (AWS Certified Solutions Architect, etc.)\n5. Build and deploy applications on the cloud\n6. Stay updated with cloud technologies and trends",
        "UX?UI_design": "1. Learn design principles and tools (Figma, Sketch, etc.)\n2. Understand user research and usability testing\n3. Master wireframing and prototyping\n4. Build a portfolio of design projects\n5. Stay updated with design trends and best practices\n6. Network with other designers and professionals in the field",
        "graphic_design": "1. Learn design software (Adobe Photoshop, Illustrator, etc.)\n2. Understand color theory and typography\n3. Master layout and composition techniques\n4. Build a portfolio of design work\n5. Stay updated with design trends and techniques\n6. Network with other designers and professionals in the field",
        "game_development": "1. Learn programming languages (C#, C++, etc.)\n2. Master game engines (Unity, Unreal Engine, etc.)\n3. Understand game design principles\n4. Build and publish games\n5. Participate in game jams\n6. Stay updated with the latest game development trends and technologies",
    }
    return maps.get(field.lower(), "Career roadmap not found for the specified field.")
