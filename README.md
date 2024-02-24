# Cross-Up

Cross-Up is an automatic reupload and cross-seed script designed for use with qBittorrent. This tool relies on Cross-seed, Autobrr/RSS feeds, and L4G Upload-Assistant.

## Overview

Cross-Up automates the process of reuploading completed torrents and initiating cross-seeding to maintain torrent availability and distribution. It is particularly useful for torrent users who manage large collections and want to ensure the longevity and availability of their content.

## Features

- Automatically triggers reupload and cross-seeding processes upon torrent completion.
- Supports integration with qBittorrent's 'Run external program on torrent completion' feature.
- Utilizes Cross-seed, Autobrr/RSS feeds, and L4G Upload-Assistant for efficient management of torrents.
- Provides flexibility through customizable configuration options.

## Prerequisites

- **Cross-seed Daemon**: Cross-seed must be set up in Daemon mode for Cross-Up to function properly.
- **qBittorrent Configuration**: Configure qBittorrent to execute Cross-Up upon torrent completion. Add the following command to the 'Run external program on torrent completion' section: `/path/to/cross-up.py "%F" "%L" "%I"`

## Usage

1. Ensure that the `config.cfg` file is properly configured to specify the desired behavior of Cross-Up.
2. Configure qBittorrent to invoke Cross-Up upon torrent completion as described in the Prerequisites section.
3. Monitor Cross-Up's execution logs to ensure proper functioning and troubleshoot any issues if necessary.

## Configuration

Before using Cross-Up, make sure to configure the `config.cfg` file according to your preferences. This file contains settings such as tracklist paths, category mappings, and other parameters used by the script.

## Command-line Parameters

Cross-Up accepts the following command-line parameters:

- `%F`: Content path
- `%L`: Category for the torrents to be reuploaded
- `%I`: InfoHash of the torrent for cross-seeding

These parameters are passed by qBittorrent when invoking Cross-Up and are used to identify and process the completed torrent.

## TO-DO

- Implement functionality to trigger Cross-Up upon category change in qBittorrent.
- Add support for additional torrent clients and seeding platforms.
- Enhance error handling and logging to improve reliability and ease of troubleshooting.

## Contributing

Contributions to Cross-Up are welcome! If you encounter any bugs, have feature requests, or want to contribute code improvements, please submit an issue or pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
