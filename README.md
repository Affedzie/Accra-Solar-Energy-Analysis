# Rooftop Solar Energy Analysis

## Project Overview

This repository contains a Python project for analyzing the potentials of rooftop solar energy in the Accra region. The project uses data from the "accra_rooftop_solarpotential.csv" dataset, which includes the following information:

- Suitable rooftop area
- Installable capacity
- Estimated yearly electricity generation
- Building type

## Dataset Description

The dataset was downloaded from NEO and contains data on solar energy potential on rooftop at the individual building structure level for a sample area of interest in Accra. 

This dataset is valuable for planning and decision-making processes, as it provides insights into the solar energy potential of different buildings in the Accra region. For more details about the methodology used to collect and process this data, please contact NEO for specific requests.

### Libraries Used

- Pandas
- Matplotlib
- Seaborn

### Data Cleaning

Missing values in the 'Peak_installable_capacity' column are handled by filling them with zeros.

### Data Visualization

A scatter plot is generated to visualize the relationship between surface area and energy potential per year. The data points are color-coded by the assumed building type.

### Calculating Average Energy Potential

The project calculates the average energy potential per year for different building types and creates a bar plot to visualize the results.

## Usage

To make the most of this project, follow these steps:

### Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Affedzie/Rooftop-Solar-Energy-Analysis.git 

```

## Install Dependencies

Ensure you have the necessary Python libraries installed. You can install them using pip:
```bash
pip install pandas matplotlib seaborn
