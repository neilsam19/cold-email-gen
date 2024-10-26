# cold-email-gen

An end-to-end Gen AI project using Llama 3.1, helping software companies send cold emails to clients.

## Use Case

The tool allows users to input the URL of a company's careers page.
The tool then extracts job listings from that page and generates personalized cold emails.

Nike needs a Principal Software Engineer and is spending time and resources in the hiring process, onboarding, training, etc

Atliq is a Software Development company that can provide a dedicated software development engineer to Nike. So, the business development executive from Atliq is going to reach out to Nike via a cold email.

## Usage

Install the libraries given in requirements.txt

There are some things you will need to change for your use case:

1. The given email template talking about your company (in chains.py)
2. the Groq API key (make a .env file to store it)
3. In my_portfolio.csv - change the links for your portfolios for each skill. Feel free to add skills as necessary.

Feel free to change the Streamlit UI as you wish.

To run the application - go to app folder and run the command "streamlit run main.py".

### Potential Errors

- ValueError: Could not connect to tenant default_tenant. Are you sure it exists?

What I did was just uninstall and reinstall chromadb with pip. You may have to install an older version of chromadb.

Please let me know of any other errors you face.

## Credits

Acknowledgements:

1. codebasics YouTube channel - https://www.youtube.com/watch?v=CO4E_9V6li0
2. https://python.langchain.com/docs/introduction/
3. https://console.groq.com/playground
4. https://docs.trychroma.com/getting-started
