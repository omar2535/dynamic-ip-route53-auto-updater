# Dynamic IP Route53 auto-updater

Script to auto-update route53 records to point to a new public IP address. Useful for home servers that have dynamically allocated IP's from internet service providers.

## Start

To run the script, first install the dependencies

```sh
pipenv install
pipenv run python main.py
```

## Scheduling the job

This script can be scheduled through CRON. Something like

```sh
0 3 * * * "pipenv run python main.py"
```

## Config files

To use this script, an account with Route53 access is needed. The `config` folder is used for credentials and hosted zone information.

## Example

Below is a screenshot of the records that this script sets for a website called `coolwebsite`.

![Example](./docs/example.png)
