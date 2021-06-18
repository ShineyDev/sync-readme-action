.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/sync-readme-action/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status" src="https://github.com/ShineyDev/sync-readme-action/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/sync-readme-action/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status" src="https://github.com/ShineyDev/sync-readme-action/workflows/Lint/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/sync-readme-action/actions?query=workflow%3ASync+event%3Apush">
            <img alt="Sync Status" src="https://github.com/ShineyDev/sync-readme-action/workflows/Sync/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/sync-readme-action</h1>
    <p align="center">A GitHub Action for synchronizing your README.* file with a readme.yml file.</p>
    <h6 align="center">Copyright 2021-present ShineyDev</h6>
    <h6 align="center">This repository is not endorsed by or affiliated with GitHub Inc. or its affiliates. "GitHub" is a registered trademark of GitHub Inc. "GitHub Actions" is a trademark of GitHub Inc.</h6>


Use
---

If you wish to use this GitHub Action as-is, place the following steps in a workflow job.


.. note::

    You should install a version of Python 3.6+ before running the GitHub Action, however this step is not required. See
    `Pre-installed Software <https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software>`_ for
    more information.


.. code:: yml

    - name: Sync README
      uses: ShineyDev/sync-readme-action@main

    - name: Push
      continue-on-error: true
      run: |
        git config user.name github-actions[bot]
        git config user.email 41898282+github-actions[bot]@users.noreply.github.com
        git add .
        git commit -m "update readme"
        git push


Once you've set up your workflow, create a `readme.yml` file in `.github/data/`. This source path can be changed via a GitHub Action input.


If you wish to use the script directly, run the following.


.. code:: sh

    $ python script.py --help
