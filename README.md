# Automated Testing Project

This project demonstrates automated testing using Selenium WebDriver with Python. It includes a simple script (`test_script.py`) that launches Google Chrome in headless mode, navigates to a test website, and prints the page title.

## Tech Stacks Used

- **Selenium**: Automates browsers. Used here to interact with the Chrome browser.
- **Python**: Programming language used for scripting.
- **ChromeDriver**: WebDriver for Chrome. Enables Selenium to control Chrome browser.
- **GitHub Actions**: Used for continuous integration to run automated tests.
- **Vercel**: Platform used for deploying the test webpage.

## Project Structure

- **test_script.py**: Python script containing Selenium WebDriver code for automated testing.
- **.github/workflows/python.yml**: GitHub Actions workflow file to automate tests on push events.
- **webpage/**: Directory containing files for the test webpage deployed on Vercel.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/automated-testing.git
   cd automated-testing
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the automated tests locally:

   ```bash
   python test_script.py
   ```

4. Deploy the test webpage to Vercel:

   - Create an account on Vercel and configure your project.
   - Deploy the contents of the `webpage/` directory to Vercel or just connect with Github and add your repository, (You can also fork this repository)

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
