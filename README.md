# PLCT-Sphinx-Components

PLCT-Sphinx-Components is a project designed to enhance your e-learning content. These extensions are Sphinx-based and focuses on online learning content, making it an ideal choice for creating interactive and engaging online courses. 

## About the Directives

All the directives provided by PLCT-Sphinx-Components are wrappers for JavaScript-based components. These components facilitate a range of interactive features, such as asking multiple choice or fill in the blank questions, python based programming in the browser, executing SQL queries, and more. This enables the creation of engaging and interactive content within your Sphinx documentation.

PLCT-Sphinx-Components heavily relies on the [Pyodide](https://pyodide.org/en/stable/) project for running Python-based code in the browser. Pyodide brings the Python runtime to the browser via WebAssembly. This allows for the execution of Python code, data analysis, visualization, and more, all directly within the browser.

## Directives

### `mchoice` Directive

The `mchoice` directive enables you to embed multiple-choice questions within your documentation.

```rst
.. mchoice::
   :answer1: Belgrade
   :answer2: Paris
   :answer3: Madrid
   :correct: 2

   What is the capital of France?
```

In this example, a multiple-choice question is created with three answer options, and the correct answer is set to "Paris".

### `fitb` Directive

The `fitb` directive allows you to insert fill-in-the-blank questions in your documentation.

```rst
.. fitb::
   :answer: OpenAI

   The GPT-3 model is developed by |blank|. 
```

In this example, a fill-in-the-blank question is created where the answer is "OpenAI".

### Note Directives

The following directives are used to add different types of notes in your documentation:

### `infonote` Directive

The `infonote` directive is employed to insert an informational note, offering a way to provide supplementary context or explanations about a specific topic.

```rst
.. infonote::

   This is an informational note.
```

---

### `suggestionnote` Directive

The `suggestionnote` directive is utilized to include a suggestion note, allowing you to provide recommendations or advice related to the content.

```rst
.. suggestionnote::

   This is a suggestion note with helpful recommendations.
```

---

### `learnmorenote` Directive

The `learnmorenote` directive serves the purpose of adding a note encouraging users to explore additional information or resources for further learning.

```rst
.. learnmorenote::

   Delve deeper into this topic by exploring additional resources.
```

---

### `technicalnote` Directive

The `technicalnote` directive is used to incorporate a technical note, which can include details or information of a technical nature.

```rst
.. technicalnote::

   This is a technical note providing in-depth technical information.
```

---

### `questionnote` Directive

The `questionnote` directive enables the addition of a note specifically tailored for posing questions or prompting further consideration.

```rst
.. questionnote::

   Here's a question to ponder: What are the implications of this concept?
```

Feel free to customize the content within the directives to suit the specific information you want to convey.


### `PyCode` Directive

The `PyCode` directive is an extension designed to execute Python code directly within web browsers. We leverage web workers and service workers to provide a seamless input/output experience. This means that students can start experimenting with Python directly in their browsers, without the need to install anything. This makes the first steps much easier.

#### Usage

```rst
.. py-code:: unique_identifier
   :packages: rich,numpy

   print('Hello, PyCode!')
```

Optional arguments include:

- `packages`: Specify additional Python packages and the environment will install it using `micropip`, a lightweight version of `pip`. This means you can use a wide range of Python packages further enhancing the learning and experimentation possibilities.

## Installation and Usage

To use the PLCT-Sphinx-Components in your Sphinx project, follow these steps:

1. Install the extension using pip:

   ```
   pip install PLCT-Sphinx-Components
   ```

2. Add the extension to your Sphinx project's `conf.py` file:

   ```python
   extensions = [
       # ... other extensions ...
       'plct-sphinx-components.extensions.multiple_choice',
       'plct-sphinx-components.extensions.fill_in_the_blank',
       'plct-sphinx-components.extensions.py_code,
   ]
   ```

3. Once the extension is enabled, you can start using the directives in your documentation files as demonstrated in the examples above.

## About

This project is maintained by Petlja and aims to enhance the educational content creation experience using Sphinx. For more information about Petlja and its initiatives, please visit [Petlja's website](https://www.petlja.org).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
