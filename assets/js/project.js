AOS.init();
/* Project Cards */

const projectcards = document.querySelector(".projectcards");

// Array of object for projects
const projects = [
  {
    title: "Globe Trotters",
    cardImage: "assets/images/project-page/quiz.jpg",
    description: "A basic frontend website for travelling.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
    Previewlink: "https://globaltrotters.netlify.app",
    Githublink: "https://github.com/ARYANJAGANI/GLOBE-TROTTERS",
  },
  {
    title: "Health Care Chatbot",
    cardImage: "assets/images/project-page/chess.jpg",
    description: "",
    tagimg: "https://image.flaticon.com/icons/png/512/643/643350.png",
    Previewlink: "https://github.com/ARYANJAGANI/questiondiagnosistkinter",
    Githublink: "https://github.com/ARYANJAGANI/questiondiagnosistkinter",
  },
  {
    title: "Mental Fitness Tracker",
    cardImage: "assets/images/project-page/flappybird.png",
    description: "",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
    Previewlink: "https://github.com/ARYANJAGANI/Mentalfitnesstracker",
    Githublink: "https://github.com/ARYANJAGANI/Mentalfitnesstracker",
  },
  {
    title: "Exercise Tracker",
    cardImage: "assets/images/project-page/exercise.jpg",
    description: "",
    tagimg: "https://miro.medium.com/max/2800/0*U2DmhXYumRyXH6X1.png",
    Previewlink: "https://github.com/ARYANJAGANI/Realtime_fitness_tracker",
    Githublink: "https://github.com/ARYANJAGANI/Realtime_fitness_tracker",
  },
  {
    title: "Weather App",
    cardImage: "assets/images/project-page/recipe.jpg",
    description: "",
    tagimg:
      "data:image/png;base64,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",
    Previewlink: "https://aryanjaganisweatherapp.netlify.app/",
    Githublink: "https://github.com/ARYANJAGANI/Weather-App",
  },
  // {
  //   title: "Poker Game",
  //   cardImage: "assets/images/project-page/poker.jpg",
  //   description: "Poker game built using typescript.",
  //   tagimg: "https://miro.medium.com/max/816/1*mn6bOs7s6Qbao15PMNRyOA.png",
  //   Previewlink: "",
  //   Githublink: "",
  // },
  {
    title: "Tic Tac Toe Game",
    cardImage: "assets/images/project-page/tic-tac-toe.png",
    description:
      "",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
    Previewlink: "https://aryanjaganistictactoeapp.netlify.app/",
    Githublink: "https://github.com/ARYANJAGANI/TIC-TAC-TOE",
  },
  // {
  //   title: "Personal Book Library",
  //   cardImage: "assets/images/project-page/book.png",
  //   description: "Personal book library app built using JavaScript.",
  //   tagimg: "https://image.flaticon.com/icons/png/512/643/643350.png",
  //   Previewlink: "",
  //   Githublink: "",
  // },
  {
    title: "SQL Projects",
    cardImage: "assets/images/project-page/sql projects.png",
    description: "SQL Data Analysis and Management Projects.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/postgresql-11-1175122.png",
    Previewlink: "https://github.com/ARYANJAGANI/sql_projects",
    Githublink: "https://github.com/ARYANJAGANI/sql_projects",
  },
  {
    title: "Masters Thesis UMBC",
    cardImage: "assets/images/project-page/masters thesis.png",
    description: "Materials and research for Master's Thesis at UMBC.",
    tagimg: "assets/images/experience-page/experience.svg",
    Previewlink: "https://github.com/ARYANJAGANI/Masters-Thesis-Umbc",
    Githublink: "https://github.com/ARYANJAGANI/Masters-Thesis-Umbc",
  },
  {
    title: "Trustworthy AI Medical Imaging",
    cardImage: "assets/images/project-page/trustworthy ai.png",
    description: "ResNet-Based Diagnosis with Grad-CAM Explanations.",
    tagimg: "assets/images/experience-page/experience.svg",
    Previewlink: "https://github.com/ARYANJAGANI/Toward-Trustworthy-AI-for-Medical-Imaging-ResNet-Based-Diagnosis-with-Grad-CAM-Explanations",
    Githublink: "https://github.com/ARYANJAGANI/Toward-Trustworthy-AI-for-Medical-Imaging-ResNet-Based-Diagnosis-with-Grad-CAM-Explanations",
  },
  {
    title: "Coastal Flooding Forecasting",
    cardImage: "assets/images/project-page/coastal flood forecasting.png",
    description: "NSF HDR Challenge: Predicting coastal flooding events.",
    tagimg: "assets/images/experience-page/experience.svg",
    Previewlink: "https://github.com/ARYANJAGANI/NSF-HDR-Challenge-Coastal-Flooding-Forecasting",
    Githublink: "https://github.com/ARYANJAGANI/NSF-HDR-Challenge-Coastal-Flooding-Forecasting",
  },
  {
    title: "BI Dashboard",
    cardImage: "assets/images/project-page/bi dashboard.png",
    description: "Business Intelligence Dashboard for data visualization.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/tableau-software-1-1175080.png",
    Previewlink: "https://github.com/ARYANJAGANI/BI-Dashboard",
    Githublink: "https://github.com/ARYANJAGANI/BI-Dashboard",
  },
  // {
  //   title: "HR Dashboard",
  //   cardImage: "assets/images/project-page/project-card.svg",
  //   description: "Human Resources analytics dashboard.",
  //   tagimg: "https://cdn.iconscout.com/icon/free/png-512/tableau-software-1-1175080.png",
  //   Previewlink: "https://github.com/ARYANJAGANI/Hr-Dashboard",
  //   Githublink: "https://github.com/ARYANJAGANI/Hr-Dashboard",
  // },
  {
    title: "Botnet Detection",
    cardImage: "assets/images/project-page/botnet detection.png",
    description: "Detecting botnets from network traffic analysis.",
    tagimg: "assets/images/experience-page/experience.svg",
    Previewlink: "https://github.com/ARYANJAGANI/Botnet-detection-From-network-traffic",
    Githublink: "https://github.com/ARYANJAGANI/Botnet-detection-From-network-traffic",
  },
  // {
  //   title: "Hack UMBC Project",
  //   cardImage: "assets/images/project-page/project-card.svg",
  //   description: "Submission for Hack UMBC.",
  //   tagimg: "assets/images/experience-page/experience.svg",
  //   Previewlink: "https://github.com/ARYANJAGANI/hack-umbc-aryan",
  //   Githublink: "https://github.com/ARYANJAGANI/hack-umbc-aryan",
  // },
  // {
  //   // title: "Live Excel Stock",
  //   // cardImage: "assets/images/project-page/project-card.svg",
  //   // description: "Live stock data tracking in Excel.",
  //   // tagimg: "assets/images/experience-page/experience.svg",
  //   // Previewlink: "https://github.com/ARYANJAGANI/live_ecxel_stock",
  //   // Githublink: "https://github.com/ARYANJAGANI/live_ecxel_stock",
  // },
  // {
  //   //   title: "733 Project",
  //   //   cardImage: "assets/images/project-page/project-card.svg",
  //   //   description: "Course project for IS 733.",
  //   //   tagimg: "assets/images/experience-page/experience.svg",
  //   //   Previewlink: "https://github.com/ARYANJAGANI/733-project",
  //   //   Githublink: "https://github.com/ARYANJAGANI/733-project",
  //   // 
  // },
  // {
  //   title: "Flipmart Dashboard",
  //   cardImage: "assets/images/project-page/project-card.svg",
  //   description: "E-commerce dashboard for Flipmart.",
  //   tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
  //   Previewlink: "https://github.com/ARYANJAGANI/flipmart_Dashboard",
  //   Githublink: "https://github.com/ARYANJAGANI/flipmart_Dashboard",
  // },
  // {
  //   // title: "IS733 UMBC",
  //   // cardImage: "assets/images/project-page/project-card.svg",
  //   // description: "IS 733 Project Repository.",
  //   // tagimg: "assets/images/experiesnce-page/experience.svg",
  //   // Previewlink: "https://github.com/ARYANJAGANI/IS733_UMBC",
  //   // Githublink: "https://github.com/ARYANJAGANI/IS733_UMBC",
  // },
  // {
  //   // title: "Namaste React",
  //   // cardImage: "assets/images/project-page/project-card.svg",
  //   // description: "Learning React JS in depth.",
  //   // tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
  //   // Previewlink: "https://github.com/ARYANJAGANI/Namaste-React",
  //   // Githublink: "https://github.com/ARYANJAGANI/Namaste-React",
  // },
  {
    title: "Wine Quality Prediction",
    cardImage: "assets/images/project-page/wine quality prediction.png",
    description: "Predicting wine quality using machine learning.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/python-2-226051.png",
    Previewlink: "https://github.com/ARYANJAGANI/WineQualityPrediction",
    Githublink: "https://github.com/ARYANJAGANI/WineQualityPrediction",
  },
  {
    title: "Iris Flower Classification",
    cardImage: "assets/images/project-page/iris flower classification.png",
    description: "Classifying Iris flower species using ML.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/python-2-226051.png",
    Previewlink: "https://github.com/ARYANJAGANI/IrisFlowerClassification",
    Githublink: "https://github.com/ARYANJAGANI/IrisFlowerClassification",
  },
  {
    title: "House Price Prediction",
    cardImage: "assets/images/project-page/house.png",
    description: "Predicting house prices using regression models.",
    tagimg: "https://cdn.iconscout.com/icon/free/png-512/python-2-226051.png",
    Previewlink: "https://github.com/ARYANJAGANI/HousePricePrediction",
    Githublink: "https://github.com/ARYANJAGANI/HousePricePrediction",
  },
  // {
  //   // title: "BE Internship Spring",
  //   // cardImage: "assets/images/project-page/project-card.svg",
  //   // description: "Spring internship project repository.",
  //   // tagimg: "assets/images/experience-page/experience.svg",
  //   // Previewlink: "https://github.com/ARYANJAGANI/be_internship_spring",
  //   // Githublink: "https://github.com/ARYANJAGANI/be_internship_spring",
  // },
  // {
  //   title: "Listing Properties Front",
  //   cardImage: "assets/images/project-page/project-card.svg",
  //   description: "Frontend for property listing application.",
  //   tagimg: "https://cdn.iconscout.com/icon/free/png-512/react-1-282599.png",
  //   Previewlink: "https://github.com/ARYANJAGANI/listing-properties-front",
  //   Githublink: "https://github.com/ARYANJAGANI/listing-properties-front",
  // },
  // {
  //   title: "Minesweeper Game",
  //   cardImage: "assets/images/project-page/minesweeper.jpg",
  //   description:
  //     "Minesweeper Game built using python Object Oriented Programming.",
  //   tagimg:
  //     "https://camo.githubusercontent.com/888e388801f947dec7c3d843942c277af25fe2b1aed1821542c4e711f210312a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67",
  //   Previewlink: "",
  //   Githublink: "",
  // },
  // {
  //   title: "Battery Life Calculator",
  //   cardImage: "assets/images/project-page/battery.png",
  //   description: "Built battery life calculator using Python.",
  //   tagimg:
  //     "https://camo.githubusercontent.com/888e388801f947dec7c3d843942c277af25fe2b1aed1821542c4e711f210312a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67",
  //   Previewlink: "",
  //   Githublink: "",
  // },
  // {
  //   title: "Movie Recommendation System",
  //   cardImage: "assets/images/project-page/movie-recommendation.jpeg",
  //   description: "Built using Tensorflow.",
  //   tagimg:
  //     "https://cdn-images-1.medium.com/max/1200/1*iDQvKoz7gGHc6YXqvqWWZQ.png",
  //   Previewlink: "",
  //   Githublink: "",
  // },
  // {
  //   title: "Music Recommendation Engine",
  //   cardImage: "assets/images/project-page/music.jpg",
  //   description: "Built using Python.",
  //   tagimg:
  //     "https://camo.githubusercontent.com/888e388801f947dec7c3d843942c277af25fe2b1aed1821542c4e711f210312a/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f632f63332f507974686f6e2d6c6f676f2d6e6f746578742e7376672f37363870782d507974686f6e2d6c6f676f2d6e6f746578742e7376672e706e67",
  //   Previewlink: "",
  //   Githublink: "",
  // },
];

// function for rendering project cards data
const showCards = () => {
  let output = "";
  projects.forEach(({ title, cardImage, Previewlink, Githublink }) => {
    output += `       
        <div class="column skill-card card" style="margin: 15px"data-aos="zoom-in-up" data-aos-easing="linear" data-aos-delay="300" data-aos-duration="600" >
          <div class="wrapper" style="background: url('${cardImage}') center / cover no-repeat;">
            <div class="header">
            </div>
            <div class="data">
              <div class="content">
              <div class="title-div">
                <h1 class="title"><a href="#">${title}</a></h1>
                </div>
            <ul class="menu-content"><br>
                  <li><a href="${Previewlink}" class="social-icon"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" viewBox="0 0 30 28" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-monitor"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg></a></li>
                  <li><a href="${Githublink}" class="social-icon"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="25" viewBox="0 0 30 28" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="feather feather-github"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg></a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>`;
  });
  projectcards.innerHTML = output;
};
document.addEventListener("DOMContentLoaded", showCards);

function myFunction() {
  // Declare variables
  var input, button, i, skillcard, card, title;
  input = document.getElementById("myInput").value;
  input = input.toUpperCase();
  skillcard = document.getElementsByClassName("skill-card");
  card = document.getElementsByClassName("card");
  title = document.getElementsByClassName("title");

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < button.length; i++) {
    if (
      button[i].innerHTML.toUpperCase().includes(input) ||
      title[i].innerHTML.toUpperCase().includes(input)
    ) {
      skillcard[i].style.display = "";
      card[i].style.display = "";
    } else {
      skillcard[i].style.display = "none";
      card[i].style.display = "none";
    }
  }
}
