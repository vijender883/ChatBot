# Contributing to the RAG Chatbot Project

First off, thank you for considering contributing! Every contribution helps us make this project better.

This document provides guidelines for contributing to the project. Please feel free to propose changes to this document in a pull request.

## How Can I Contribute?

There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into the main project.

### Reporting Bugs

- **Ensure the bug was not already reported** by searching the GitHub Issues.
- If you're unable to find an open issue addressing the problem, open a new one. Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue with the `enhancement` label.
- Clearly describe the enhancement and the motivation for it.

### Your First Code Contribution

Unsure where to begin contributing? You can start by looking through `good first issue` and `help wanted` issues.

## Contribution Workflow

We use the standard GitHub `fork-and-pull` workflow. Here’s how to get started with your first contribution:

### 1. Fork the Repository

First, you'll need your own copy of the repository. Click the "Fork" button on the top right of the main repository page on GitHub. This will create a copy of the repository in your own GitHub account.

### 2. Clone Your Fork

Now, clone your forked repository to your local machine.

```bash
git clone https://github.com/YOUR_USERNAME/ChatBot.git
cd ChatBot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Create a New Branch

It's important to create a new branch for each feature or bug fix you work on. This keeps your changes organized and separate from the `main` branch.

```bash
git checkout -b your-descriptive-branch-name
```

For example, `git checkout -b fix-pdf-parsing-bug` or `git checkout -b add-new-llm-support`.

### 4. Make Your Changes

Now you can make your changes to the code.

- Make sure to follow the coding style of the project.
- Add comments to your code where necessary.
- If you add a new feature, please add tests for it.

### 5. Commit Your Changes

Once you are happy with your changes, commit them with a clear and descriptive commit message.

```bash
git add .
git commit -m "feat: Describe your feature or fix"
```

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification. Common prefixes include `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`.

### 6. Push to Your Fork

Push your changes to your forked repository on GitHub.

```bash
git push origin your-descriptive-branch-name
```

### 7. Submit a Pull Request (PR)

- Go to your forked repository on GitHub.
- Click the "Compare & pull request" button that appears for your new branch.
- Make sure the base repository is the original `ChatBot` repository and the head repository is your fork.
- Add a clear title and description for your pull request, explaining the changes you've made.
- Click "Create pull request".

Our team will then review your contribution. We may suggest some changes or improvements.

Thank you for your contribution!
