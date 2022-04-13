# **Comment Unused Code**

Using the `main.py` script, we can comment any unused code.

## **Prerequisites**

-  Python >= 3.6
-  Vulture (python package)

## **Overview**

To run this script you will need to have Python and Vulture installed on your machine. The instructions to setup Python can be found online. After installing Python, run the following command to install Vulture.

```
pip install vulture
```

## **Implementation**

1. Clone the repository & open the repository root directory in terminal.

2. To comment the unused the code. Follow the following pattern.

    ```
    <python> <main.py> <class file path> <usage file path>
    ```

3. We have a class file named `class_file.py`. The usage file is named `usage_file.py`.

4. In `usage_file.py`, we are calling methods from the `class_file.py` which are 
    -    displayPublicMembers()

5. To comment the following unused methods in `class_file.py`, which are
    -   _displayProtectedMembers()
    -   accessPrivateMembers()

6. Let's run the script.

    ```
    python main.py class_file.py usage_file.py
    ```

7. The above mentioned unused methods are commented & and we can check the code in `class_file.py`.

8. The output we get after running the above mentioned command.

    ```
    <--- Unused Methods --->

    1) _displayProtectedMembers

    2) accessPrivateMembers

    ```