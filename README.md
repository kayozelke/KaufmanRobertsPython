# Kaufman-Roberts Algorithm Implementation

This repository contains a Python implementation of the Kaufman-Roberts algorithm, used for calculating performance metrics in telecommunications and other related queuing systems.

## Overview

The Kaufman-Roberts algorithm is commonly used for blocking probability calculations in multi-service loss systems. This implementation includes functions to calculate key variables, such as `x`, `P`, and `b`, which are essential for analyzing system performance.

## Features

- **calc_x**: Computes the recursive sequence `x` based on system capacity `V`, number of service types `M`, arrival rates `a`, and service times `t`.
- **calc_p0**: Calculates the probability `P(0)` that there are no occupied resources in the system.
- **calc_pn**: Computes the probability distribution `P(n)` for `n` resources being occupied.
- **calc_bn**: Calculates the blocking probability for a given service type.
- **calc_all**: Combines all calculations and outputs the results.

## How to Use

1. **Parameters:**
   - `M`: The number of different service types.
   - `V`: The total capacity of the system.
   - `a`: A list of arrival rates for each service type.
   - `t`: A list of service times for each service type.

2. **Example Usage:**

   ```python
   M = 2
   V = 3
   t = [[1, 2]]
   a = [[0.4, 1], [1, 2]]

   for item in a:
       for item2 in t:
           print("#### M:", M)
           print("#### V:", V)
           print("#### a:", item)
           print("#### t:", item2)
           calc_all(M, V, item, item2)
