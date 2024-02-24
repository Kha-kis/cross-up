# Cross-Up

Cross-Up is an automatic reupload and cross-seed script designed for use with torrent clients like qBittorrent and rTorrent. This tool relies on Cross-seed, Autobrr/RSS feeds, and L4G Upload-Assistant.

## Overview

Cross-Up automates the process of reuploading completed torrents and initiating cross-seeding to maintain torrent availability and distribution. It is particularly useful for torrent users who manage large collections and want to ensure the longevity and availability of their content.

## Features

- Automatically triggers reupload and cross-seeding processes upon torrent completion.
- Supports integration with torrent clients' 'Run external program on torrent completion' feature.
- Utilizes Cross-seed, Autobrr/RSS feeds, and L4G Upload-Assistant for efficient management of torrents.
- Provides flexibility through customizable configuration options.

## Prerequisites

- **Cross-seed Daemon**: Cross-seed must be set up in Daemon mode for Cross-Up to function properly.
- **Torrent Client Configuration**:
  - For qBittorrent, configure it to execute Cross-Up upon torrent completion. Add the following command to the 'Run external program on torrent completion' section:
```bash
/usr/bin/python3 -u /path/to/cross-up.py "%F" "%L" "%I"`
```
  `%F`: Content path

  `%L`: Category for the torrents to be reuploaded

  `%I`: InfoHash of the torrent for cross-seeding

  - For rTorrent, follow these steps:
    1. Add the following line to your `.rtorrent.rc` file to define a method for retrieving the label:
       ```bash
       echo 'method.insert=label.get_label,simple,"d.custom1="' >> ~/.rtorrent.rc
       ```
    2. Add the following line to set up the execution of `cross-up.py`:
       ```bash
       echo 'method.set_key=event.download.finished,cross_seed,"execute={/usr/bin/python3,-u,/path/to/cross-up.py,--data-path=,$d.get_base_path=,--label=,$d.custom1=,--hash=,$d.hash=}"' >> ~/.rtorrent.rc
       ```
       Ensure to replace `/path/to/cross-up.py` with the actual path to your Python script.

## Usage

1. Ensure that the `config.cfg` file is properly configured to specify the desired behavior of Cross-Up.
2. Configure your torrent client(s) to invoke Cross-Up upon torrent completion as described in the Prerequisites section.
3. Monitor Cross-Up's execution logs to ensure proper functioning and troubleshoot any issues if necessary.

## Configuration

Before using Cross-Up, make sure to configure the `config.cfg` file according to your preferences. This file contains settings such as clients, trackersm category/label mappings, and other parameters used by the script.


## TO-DO

- Implement functionality to trigger Cross-Up upon category change in qBittorrent.
- Add support for additional torrent clients and seeding platforms.
- Enhance error handling and logging to improve reliability and ease of troubleshooting.

## Contributing

Contributions to Cross-Up are welcome! If you encounter any bugs, have feature requests, or want to contribute code improvements, please submit an issue or pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
