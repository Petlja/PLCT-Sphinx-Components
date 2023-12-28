# PLCT-Sphinx-Components

The PLCT-Sphinx-Components a project designed to enhance the capabilities of Sphinx, a widely used documentation generation tool. This extension provides custom directives that are particularly useful for creating e-learning content within your Sphinx documentation.

## About the Directives

All the directives provided by PLCT-Sphinx-Components are wrappers for PLCT-Web-Components. This means that they leverage the functionality of PLCT-Web-Components to provide interactive and engaging features for your Sphinx documentation.

The `mchoice` and `fitb` directives, for instance, are designed to create interactive educational content within your documentation. They are implemented as wrappers around the corresponding web components provided by PLCT-Web-Components, thus allowing you to seamlessly integrate these features into your Sphinx documentation.

## Directives

### `mchoice` Directive

The `mchoice` directive enables you to embed multiple-choice questions within your documentation. This is particularly handy for creating interactive educational content. Here's an example of how to use this directive:

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

The `fitb` directive allows you to insert fill-in-the-blank questions in your documentation. This is a great way to create interactive exercises. Here's an example of how to use this directive:

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

The `PyCode` directive is an extension designed to execute Python code directly within web browsers using Pyodide. 

#### Usage

```rst
.. py-code:: unique_identifier
   :packages: rich,numpy

   print('Hello, PyCode!')
```

Optional arguments include:

- `packages`: Specify additional Python packages that should be available in the Python environment. Multiple packages can be included and are separated by commas.

The resulting HTML output includes an interactive code block that executes Python code using Pyodide.


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
   ]
   ```

3. Once the extension is enabled, you can start using the `mchoice` and `fitb` directives in your documentation files as demonstrated in the examples above.


This will render a fill-in-the-blank question where the answer is "Python".

Feel free to explore the capabilities of the PLCT-Sphinx-Components to create engaging and interactive e-learning content within your Sphinx documentation.

## About

This project is maintained by Petlja and is aimed at enhancing the educational content creation experience using Sphinx. For more information about Petlja and its initiatives, please visit [Petlja's website](https://www.petlja.org).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---
