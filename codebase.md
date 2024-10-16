# .gitignore

```
.vscode
```

# assets\logo\editable\variation-1.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-2.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-3.ai

This is a binary file of the type: Binary

# assets\logo\editable\variation-4.ai

This is a binary file of the type: Binary

# assets\logo\svg\variation-1.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-2.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-3.svg

This is a file of the type: SVG Image

# assets\logo\svg\variation-4.svg

This is a file of the type: SVG Image

# changes.md

```md
# CRAC Bot Changelog

## Latest Updates

+ Added restart command
+ Updated shutdown command to disconect from all voice channels
+ Updated start command to set RPC to the help info
```

# config.json

```json
{
    "defaults": {
        "prefix": "?"
    },

    "bot_version": "0.4.6",
    "bot_name": "CRAC   ",
    "tts_mode":"fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    
    "colors": {
      "Red": "#FFB3BA",
      "Coral": "#FFCCB6",
      "Orange": "#FFE5B4",
      "Gold": "#FFF1B5",
      "Yellow": "#FFFFD1",
      "Lime": "#DCFFB8",
      "Green": "#BAFFC9",
      "Teal": "#B5EAD7",
      "Cyan": "#C7F2FF",
      "Blue": "#B5DEFF",
      "Navy": "#C5CAE9",
      "Purple": "#D0B8FF",
      "Magenta": "#F2B5D4",
      "Pink": "#FFCCE5",
      "Gray": "#E0E0E0",
      "Lavender": "#E6E6FA"
    },

    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
```

# crac.db

This is a binary file of the type: Binary

# db_manager\__intit__.py

```py

```

# db_manager\feedback.py

```py
import sqlite3
import datetime


def add_feedback(user_id: str, message: str) -> bool:
    """Uses SQLite to add user's feedback to feedback db table

    ### Params:
        `used_id`  `str`   The user id of the person who submitted the feedback.
        `message`  `str`   The name of the command that the user ran.

    ### Return:
        Returns a bool (True on success)
    """

    datetime_value = datetime.datetime.today().now().__format__("%S:%M:%H %d/%m/%y")

    db_connection = sqlite3.connect("./crac.db")
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        f'INSERT INTO feedback VALUES (\'{user_id}\', "{message}", "{datetime_value}")'
    )
    db_connection.commit()

    return True

```

# db_manager\history.py

```py
import sqlite3
import datetime
import json

def add_history(user_id: int, command: str, arguments: list[str] = ["none"]) -> bool:
    """Uses SQLite to add user command to history of commands ran

    ### Params:
        `user_id`  `int`   The user id of the person who ran the command.
        `command`  `str`   The name of the command that the user ran.
        `arguments`  `list[str]`   The arguments passed in to the command, defaults to ["none"].

    ### Return:
        Returns a bool (True on success)
    """
    args_json = json.dumps(arguments)
    datetime_value = datetime.datetime.now().strftime("%S:%M:%H %d/%m/%y")
    
    db_connection = sqlite3.connect("./crac.db")
    db_cursor = db_connection.cursor()
    
    try:
        db_cursor.execute(
            "INSERT INTO history (user_id, command, arguments, datetime) VALUES (?, ?, ?, ?)",
            (user_id, command, args_json, datetime_value)
        )
        db_connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"ERROR_LOG: SQLite error: {e}")
        return False
    finally:
        db_connection.close()
```

# db_manager\usage.py

```py
import sqlite3
from typing import List, Tuple
import json

DB_PATH = "./crac.db"


def get_db_connection():
    """Create and return a database connection."""
    return sqlite3.connect(DB_PATH)


def execute_query(query: str, params: Tuple = (), fetch: bool = False):
    """Execute a SQL query and optionally fetch results."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return True


def get_usage(command_name: str) -> Tuple[str, str, str]:
    """Get usage information for a specific command.

    Args:
        command_name (str): The name of the command to retrieve.

    Returns:
        Tuple[str, str, str]: A tuple containing (command_name, arguments, level).
        Returns None if the command is not found.
    """
    query = "SELECT command_name, arguments, level FROM usage WHERE command_name = ?"
    result = execute_query(query, (command_name,), fetch=True)
    return result[0] if result else None


def get_all_usages() -> List[Tuple[str, str, str]]:
    """Get usage information for all commands.

    Returns:
        List[Tuple[str, str, str]]: A list of tuples, each containing (command_name, arguments, level).
    """
    query = "SELECT command_name, arguments, level FROM usage"
    return execute_query(query, fetch=True)


def add_usage(command_name: str, arguments: List[str], level: int) -> bool:
    """Add usage information for a command.

    Args:
        command_name (str): The name of the command to add.
        arguments (List[str]): The list of arguments the command accepts.
        level (int): The permission level of the command (0-3).

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    if not 0 <= level <= 3:
        raise ValueError("Level must be between 0 and 3")

    query = "INSERT INTO usage (command_name, arguments, level) VALUES (?, ?, ?)"
    args_json = json.dumps(arguments)
    return execute_query(query, (command_name, args_json, str(level)))
```

# launcher.py

```py
from src.bot import client

client.run("MTI4OTkyMTQ3NjYxNDU1MzY3Mg.GNo3VX.kjVPN-1ri34TtfuWZ-ADqhSeW56fARaLu7pMnk")
```

# LICENSE

```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2024 Iona M.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

# README.md

```md
# CRAC Bot

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Commands](#commands)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Project Structure](#project-structure)
8. [Dependencies](#dependencies)
9. [Development](#development)
10. [Contributing](#contributing)
11. [License](#license)
12. [Support](#support)
13. [Creator](#creator)

## Introduction

CRAC Bot is a versatile, all-purpose Discord bot designed to enhance server management and user interaction. Currently in active development, CRAC Bot offers a wide range of features from moderation tools to fun commands, making it a valuable addition to any Discord server.

## Features

1. **Server Moderation**
   - Kick users
   - Ban and unban users
   - Timeout users
   - Nickname management

2. **User Interaction**
   - Character information lookup
   - Text-to-speech functionality
   - Music playback from YouTube
   - User profile display

3. **Bot Management**
   - Customizable bot status
   - Start/shutdown commands
   - Feedback system

4. **Message Handling**
   - Logging of message edits and deletions
   - Inappropriate word detection and filtering

5. **Voice Channel Integration**
   - Join and leave voice channels
   - Play audio in voice channels

6. **Customization**
   - Configurable command prefix
   - Guild-specific settings

## Commands

Here's a detailed list of available commands:

1. `?help`: Displays a help message with all available commands and their usage.

2. `?kick @user [reason]`: Kicks the mentioned user from the server. Requires kick permissions.
   
3. `?ban @user [reason]`: Bans the mentioned user from the server. Requires ban permissions.
   
4. `?unban @user`: Unbans the specified user from the server. Requires ban permissions.
   
5. `?timeout @user <duration> <unit> [reason]`: Timeouts the mentioned user for the specified duration. Requires moderate members permission.
   
6. `?shutdown`: Shuts down the bot. Requires administrator permissions.
   
7. `?start`: Starts the bot if it's offline. Requires administrator permissions.
   
8. `?charinfo [character]`: Provides detailed information about the specified character, including Unicode data.
   
9. `?tts [message]`: Converts the given text to speech and plays it in the user's current voice channel.
   
10. `?play [youtube_url]`: Plays audio from the specified YouTube video in the user's current voice channel.
    
11. `?join`: Makes the bot join the user's current voice channel.
    
12. `?leave`: Makes the bot leave the current voice channel.
    
13. `?profile @user`: Displays detailed profile information about the mentioned user.
    
14. `?nick @user [new_nickname]`: Changes the nickname of the mentioned user. Requires manage nicknames permission.
    
15. `?feedback [message]`: Allows users to submit feedback about the bot, which is stored in a database.

## Installation

1. Clone the repository:
   \`\`\`
   git clone https://github.com/your-username/crac-bot.git
   \`\`\`

2. Navigate to the project directory:
   \`\`\`
   cd crac-bot
   \`\`\`

3. Install the required dependencies:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Set up your Discord bot token:
   - Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a bot for your application and copy the bot token
   - Create a `config.json` file in the project root and add your token:
     \`\`\`json
     {
         "token": "YOUR_BOT_TOKEN_HERE"
     }
     \`\`\`

5. Set up the SQLite database:
   \`\`\`
   python setup/create_feedback_table.py
   python setup/create_history_table.py
   python setup/create_usage_table.py
   \`\`\`

## Usage

1. Run the bot:
   \`\`\`
   python launcher.py
   \`\`\`

2. Invite the bot to your Discord server:
   - Go to the OAuth2 URL generator in your Discord Developer Portal
   - Select the "bot" scope and the necessary permissions
   - Use the generated URL to invite the bot to your server

3. Once the bot is in your server, use `?help` to see all available commands.

## Configuration

The `config.json` file contains important settings for the bot:

\`\`\`json
{
    "defaults": {
        "prefix": "?"
    },
    "bot_version": "0.4.5",
    "bot_name": "CRAC",
    "tts_mode": "fast",
    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
\`\`\`

- `defaults.prefix`: The default command prefix for the bot.
- `bot_version`: The current version of the bot.
- `bot_name`: The name of the bot.
- `tts_mode`: The mode for text-to-speech functionality ("fast" or "slow").
- `guilds`: Guild-specific settings, including custom prefixes.

## Project Structure

- `main/bot.py`: The main bot file containing command implementations and event handlers.
- `launcher.py`: The entry point for running the bot.
- `db_manager/`: Directory containing database management modules.
- `setup/`: Directory containing database setup scripts.
- `temp/audio/`: Directory for temporary audio files used by the TTS feature.
- `website/`: Directory containing HTML files for the bot's website.

## Dependencies

CRAC Bot relies on several Python libraries:

- discord.py: The core library for interacting with the Discord API.
- Pillow: Used for image manipulation in the `charinfo` command.
- gTTS: Google Text-to-Speech library for the TTS feature.
- yt_dlp: YouTube downloader used for the music playback feature.
- rich: Used for console output formatting and logging.
- langdetect: Used for language detection in the TTS feature.

For a complete list of dependencies, refer to the `requirements.txt` file.

## Development

CRAC Bot is under active development with nearly daily updates. The development process includes:

- Regular feature additions and improvements
- Bug fixes and performance optimizations
- Refactoring for better code organization and maintainability
- Implementation of user feedback and feature requests

Future development plans include:
- Implementing a music queue system
- Adding more fun and interactive commands
- Improving error handling and user feedback
- Enhancing the configuration system for more granular control

## Contributing

We welcome contributions to CRAC Bot! Here's how you can contribute:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with clear, descriptive commit messages
4. Push your changes to your fork
5. Submit a pull request to the main repository

Please ensure your code adheres to the existing style conventions and includes appropriate tests.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for the full license text.

## Support

If you need help or want to report a bug, you can:

1. Open an issue on this GitHub repository
2. Join our support Discord server (link to be added)
3. Contact us via email at crac@nerd-bear.org

## Creator

CRAC Bot is created and maintained by Nerd Bear. For more information about the creator and other projects, visit [nerd-bear.org](https://nerd-bear.org).

---

CRAC Bot © 2024 by Nerd Bear. All rights reserved.
```

# setup\clear_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE feedback")
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\clear_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE history")
db_cursor.execute("CREATE TABLE history(user_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\clear_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("DROP TABLE usage")
db_cursor.execute("CREATE TABLE usage(command_name, arguments, level)")
db_connection.commit()
```

# setup\create_feedback_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE feedback(used_id, message, datetime)")
db_connection.commit()
```

# setup\create_history_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE history(user_id, command, arguments, datetime)")
db_connection.commit()
```

# setup\create_usage_table.py

```py
import sqlite3

db_connection = sqlite3.connect("./crac.db")
db_cursor = db_connection.cursor()
db_cursor.execute("CREATE TABLE usage(command_name, arguments, level)")
db_connection.commit()
```

# src\bot.py

```py
"""
About
CRAC Bot: A versatile Discord bot for server management and user interaction. Features include moderation tools, customizable status, character info lookup, and message logging. Actively developed with frequent updates. Created by Nerd Bear for enhancing Discord communities.

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "richPrinted page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2024 Iona M.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at  

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import asyncio
import datetime
import json
import os
import random
import sys
import tempfile
import unicodedata
from collections import Counter

import discord
import yt_dlp
from deep_translator import GoogleTranslator
from discord.ui import Button, Select, Modal, TextInput, View
from gtts import gTTS
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from PIL import Image, ImageDraw, ImageFont
from rich import print as richPrint
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from db_manager import history, feedback
from src.utils.helpers import *
from src.cogs.help import help_command

CONFIG_PATH = "config.json"
FOOTER_TEXT = "This bot is created and hosted by Nerd Bear"
FOOTER_ICON = "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"


log_info("Loading Config")
config = load_config(CONFIG_PATH)
log_info("Completed loading config")

log_info("Loading default values into memory")
color_manager = ColorManager(config)
BOT_PREFIX = config["defaults"].get("prefix", "?")
BOT_NAME = config.get("bot_name", "CRAC Bot")
BOT_VERSION = config.get("bot_version", "1.0.0")
TTS_MODE = config.get("tts_mode", "normal")
LOGGING_CHANNEL_ID = int(config.get("log_channel_id", 0))
DetectorFactory.seed = config.get("tts_detector_factory_seed", 0)

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
console = Console()

bot_active = True
log_info("Completed loading default values into memory")


@client.event
async def on_ready():
    markdown = Markdown(f"# Discord {BOT_NAME} version {BOT_VERSION}")
    console.print(markdown)

    info_text = await get_info_text(BOT_NAME, BOT_VERSION, BOT_PREFIX, client.user.name, client.user.id, round(client.latency*1000), len(client.guilds))
    panel = Panel(
        info_text, title=f"{BOT_NAME} v{BOT_VERSION} Initialization Info", expand=False
    )

    console.print(panel)

    channel = client.get_channel(LOGGING_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"{BOT_NAME} v{BOT_VERSION} Initialization Info",
            description=info_text,
            color=color_manager.get_color("Green"),
            timestamp=datetime.datetime.utcnow(),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await channel.send(embed=embed)

    await client.change_presence(
        activity=discord.Game(name=f"Run {BOT_PREFIX}help for help")
    )


@client.event
async def on_message(message: discord.Message):
    global bot_active

    if message.author == client.user:
        return

    if not message.content.startswith(BOT_PREFIX):
        if bot_active == False:
            return
        content = message.content.lower()
        if any(word in content for word in ["nigger", "nigga", "negro", "nigro"]):
            await handle_inappropriate_word(message)
        return

    if message.content.startswith("?") and len(message.content.strip()) <= 1:
        return

    if not bot_active and message.content != f"{BOT_PREFIX}start":
        embed = discord.Embed(
            title="Bot Offline",
            description=f"{BOT_NAME} is currently offline. Use {BOT_PREFIX}start to activate.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    command = message.content.split()[0][len(BOT_PREFIX) :].lower()
    args = message.content.split()[1:]

    history.add_history(message.author.id, command, args)

    if command == "help":
        await help_command(message, BOT_PREFIX, BOT_NAME, BOT_VERSION, FOOTER_TEXT, FOOTER_ICON, color_manager)

    elif command == "timeout":
        await timeout_command(message)

    elif command == "kick":
        await kick_command(message)

    elif command == "ban":
        await ban_command(message)

    elif command == "unban":
        await unban_command(message)

    elif command == "shutdown":
        await shutdown_command(message)

    elif command == "start":
        await start_command(message)

    elif command == "charinfo":
        await charinfo_command(message)

    elif command == "join":
        await join_vc_command(message)

    elif command == "leave":
        await leave_vc_command(message)

    elif command == "tts":
        await tts_command(message)

    elif command == "play":
        await play_command(message)

    elif command == "profile":
        await profile_command(message)

    elif command == "nick":
        await nick_command(message)

    elif command == "feedback":
        await feedback_command(message)

    elif command == "restart":
        await restart_command(message)

    elif command == "translate":
        await translate_command(message)

    elif command == "ping":
        await ping_command(message)

    else:
        embed = discord.Embed(
            title="Invalid Command",
            description=f"The command you are running is not valid. Please run `?help` for a list of commands and their usages!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return


async def handle_inappropriate_word(message: discord.Message):
    user = message.author
    channel = message.channel

    dm_embed = discord.Embed(
        title="Inappropriate Word Detected",
        description=f"{BOT_NAME} has detected an inappropriate word! Please do not send racist words in our server! Moderators have been informed!",
        color=0xFF697A,
    )
    dm_embed.add_field(
        name="Rules",
        value="Please read our rules before sending such messages!",
        inline=False,
    )
    dm_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    try:
        await user.send(embed=dm_embed)
    except discord.errors.Forbidden:
        pass

    await message.delete()

    channel_embed = discord.Embed(
        title="Inappropriate Word Detected",
        description=f"User {user.mention} tried to send a word that is marked not allowed!",
        color=0xFF697A,
    )
    channel_embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=channel_embed)


async def kick_command(message: discord.Message):
    if not message.author.guild_permissions.kick_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to kick. Usage: {BOT_PREFIX}kick @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    reason = " ".join(message.content.split()[2:]) or "No reason provided"

    try:
        await member.send(
            embed=discord.Embed(
                title="You've wBeen Kicked",
                description=f"You were kicked from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.kick(reason=reason)
    embed = discord.Embed(
        title="User Kicked",
        description=f"{member.mention} has been kicked.\nReason: {reason}",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def ban_command(message: discord.Message):
    if not message.author.guild_permissions.ban_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to ban. Usage: {BOT_PREFIX}ban @user [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    reason = " ".join(message.content.split()[2:]) or "No reason provided"

    try:
        await member.send(
            embed=discord.Embed(
                title="You've Been Banned",
                description=f"You were banned from {message.guild.name}.\nReason: {reason}",
                color=color_manager.get_color("Red"),
            )
        )
    except:
        pass

    await member.ban(reason=reason)
    embed = discord.Embed(
        title="User Banned",
        description=f"{member.mention} has been banned.\nReason: {reason}",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def shutdown_command(message: discord.Message):
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    bot_active = False
    await client.change_presence(status=discord.Status.invisible)

    for vc in client.voice_clients:
        await vc.disconnect()

    embed = discord.Embed(
        title=f"{BOT_NAME} Shutting Down",
        description=f"{BOT_NAME} is now offline.",
        color=color_manager.get_color("Red"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def start_command(message: discord.Message):
    global bot_active
    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    bot_active = True
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name=f"Run {BOT_PREFIX}help for help"),
    )
    embed = discord.Embed(
        title=f"{BOT_NAME} Starting Up",
        description=f"{BOT_NAME} is now online.",
        color=color_manager.get_color("Green"),
        timestamp=datetime.datetime.utcnow(),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def charinfo_command(message: discord.Message):

    try:
        argument_text = " ".join(message.content.split()[1:])
        char_text = argument_text[0]
    except IndexError:
        await message.channel.send(
            embed=discord.Embed(
                title="ERROR",
                color=color_manager.get_color("Blue"),
                description="Please provide a character to get information about.",
            )
        )
        return

    unicode_value = ord(char_text)
    char_name = unicodedata.name(char_text, "Could not find name!")
    char_category = unicodedata.category(char_text)

    unicode_escape = f"\\u{unicode_value:04x}"
    unicode_escape_full = f"\\U{unicode_value:08x}"
    python_escape = repr(char_text)

    embed = discord.Embed(
        color=color_manager.get_color("Blue"),
        title="Character info",
        type="rich",
        description=f"Information on character: {char_text}",
    )

    embed.add_field(name="Original character", value=char_text, inline=True)
    embed.add_field(name="Character name", value=char_name, inline=True)
    embed.add_field(name="Character category", value=char_category, inline=True)
    embed.add_field(name="Unicode value", value=f"U+{unicode_value:04X}", inline=True)
    embed.add_field(name="Unicode escape", value=unicode_escape, inline=True)
    embed.add_field(name="Full Unicode escape", value=unicode_escape_full, inline=True)
    embed.add_field(name="Python escape", value=python_escape, inline=True)

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    image_path = get_char_image(char_text)

    if image_path:
        file = discord.File(image_path, filename="character.png")
        embed.set_thumbnail(url="attachment://character.png")
    else:
        file = None

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    await message.channel.send(embed=embed, file=file)

    if image_path and os.path.exists(image_path):
        os.remove(image_path)


async def unban_command(message: discord.Message):

    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Please mention a user to unban. Usage: {BOT_PREFIX}unban @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0]
    invite = message.channel.create_invite(reason="Invite unbanned user")

    try:
        await member.send(
            embed=discord.Embed(
                title="You've Been unbanned",
                description=f"You were unbanned from {message.guild.name}",
                color=color_manager.get_color("Green"),
            ).add_field(name="Invite link", value=invite)
        )
    except:
        pass

    try:
        await message.guild.unban(user=member)

    except discord.errors.Forbidden as e:
        embed = discord.Embed(
            title="Forbidden",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.NotFound as e:
        embed = discord.Embed(
            title="Not found",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.HTTPException as e:
        embed = discord.Embed(
            title="Unknown",
            description=f"Could not unban, {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    embed = discord.Embed(
        title="User Unbanned",
        description=f"{member.mention} has been unbanned.",
        color=color_manager.get_color("Red"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def timeout_command(message: discord.Message):
    if not message.author.guild_permissions.moderate_members:
        embed = discord.Embed(
            title="Permission Denied",
            description="You don't have permission to use this command.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    args = message.content.split()[1:]
    if len(args) < 3:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}timeout @user <duration> <unit> [reason]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    member = message.mentions[0] if message.mentions else None
    if not member:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Please mention a user to timeout.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        duration = int(args[1])
        unit = args[2].lower()

    except ValueError:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Duration must be a number.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    reason = " ".join(args[3:]) if len(args) > 3 else "No reason provided"

    if message.author.top_role <= member.top_role:
        embed = discord.Embed(
            title="Permission Denied",
            description="You cannot timeout this user as they have an equal or higher role.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    time_units = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}
    if unit not in time_units:
        embed = discord.Embed(
            title="Invalid Usage",
            description="Invalid time unit. Use 's' for seconds, 'm' for minutes, 'h' for hours, or 'd' for days.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    time_delta = datetime.timedelta(**{time_units[unit]: duration})

    try:
        await member.timeout(time_delta, reason=reason)
        embed = discord.Embed(
            title="User Timed Out",
            description=f"{member.mention} has been timed out for {duration}{unit}.\nReason: {reason}",
            color=color_manager.get_color("Green"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    except discord.errors.Forbidden:
        embed = discord.Embed(
            title="Permission Error",
            description="I don't have permission to timeout this user.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    except discord.errors.HTTPException:
        embed = discord.Embed(
            title="Error",
            description="Failed to timeout the user. The duration might be too long.",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)

    try:
        await member.timeout(time_delta, reason=reason)
        embed = discord.Embed(
            title="You were timed out",
            description=f"You (aka {member.mention}) have been timed out for {duration}{unit}.",
            color=color_manager.get_color("Green"),
        )
        embed.add_field(name="reason", value=reason, inline=True)
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await member.send(embed=embed)

    except:
        pass


async def join_vc_command(message: discord.Message):
    try:
        channel = client.get_channel(message.author.voice.channel.id)
        await channel.connect()
    except Exception as e:
        richPrint(e)


async def leave_vc_command(message: discord.Message):
    try:
        await message.guild.voice_client.disconnect()
    except Exception as e:
        pass


async def tts_command(message: discord.Message):
    text = " ".join(message.content.split()[1:])

    if not text:
        embed = discord.Embed(
            title="Missing arguments",
            description=f"Please make sure you pass some text for the TTS command. Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return
        return

    output_file = f"./temp/audio/{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}.mp3"

    try:
        text_to_speech(text, output_file, TTS_MODE)
    except Exception as e:
        embed = discord.Embed(
            title="Error occurred",
            description=f"A issue occurred during the generation of the Text-to-Speech mp3 file! Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        voice_channel = message.author.voice.channel
    except:
        embed = discord.Embed(
            title="Join voice channel",
            description=f"Please join a voice channel to use this command! Usage: {BOT_PREFIX}tts [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        vc = await voice_channel.connect()
    except discord.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    vc.play(
        discord.FFmpegPCMAudio(source=output_file),
        after=lambda e: asyncio.run_coroutine_threadsafe(vc.disconnect(), client.loop),
    )

    while vc.is_playing():
        await asyncio.sleep(0.1)

    if os.path.exists(output_file):
        os.remove(output_file)

    embed = discord.Embed(
        title="Ended TTS",
        description=f"Successfully generated and played TTS file. Disconnecting from <#{voice_channel.id}>",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)
    return


async def play_command(message: discord.Message):
    args = message.content.split(" ", 1)
    if len(args) < 2:
        await message.channel.send("Please provide a YouTube URL or search term.")
        return

    query = args[1]

    try:
        voice_channel = message.author.voice.channel
        if not voice_channel:
            raise AttributeError
    except AttributeError:
        embed = discord.Embed(
            title="Join voice channel",
            description="Please join a voice channel to use this command!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        vc = await voice_channel.connect()
    except discord.ClientException:
        vc = message.guild.voice_client

    if vc.is_playing():
        vc.stop()

    try:
        with yt_dlp.YoutubeDL({"format": "bestaudio", "noplaylist": "True"}) as ydl:
            info = ydl.extract_info(query, download=False)
            URL = info["url"]
            title = info["title"]
    except Exception as e:
        embed = discord.Embed(
            title="Error occurred",
            description=f"An issue occurred while trying to fetch the audio: {str(e)}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    vc.play(
        discord.FFmpegPCMAudio(
            URL,
            **{
                "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
                "options": "-vn",
            },
        )
    )

    embed = discord.Embed(
        title="Now Playing",
        description=f"Now playing: {title}",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def profile_command(message: discord.Message):
    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        user = message.mentions[0]

    except Exception as e:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    try:
        fetched_user = await client.fetch_user(user.id)

    except discord.errors.NotFound as e:
        embed = discord.Embed(
            title="Not found",
            description=f"Error occurred while fetching user. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except discord.errors.HTTPException as e:
        embed = discord.Embed(
            title="Unknown Error",
            description=f"Error occurred while fetching user, but this exception does not have defined behavior. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if user not in message.guild.members:
        embed = discord.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {BOT_PREFIX}profile @user",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    avatar = user.avatar
    name = user.display_name
    username = user.name
    user_id = user.id
    status = user.status
    creation = user.created_at.strftime("%d/%m/%y %H:%M:%S")
    badges = [badge.name for badge in user.public_flags.all()]
    banner_url = None
    top_role = "<@&" + str(user.roles[-1].id) + ">"
    roles: list[str] = []
    print(user.premium_since)
    roles_str = ""

    for role in user.roles:
        roles.append(f"<@&{role.id}>")

    roles.pop(0)  # Removes @everyone role

    for i in range(len(roles)):
        roles_str = roles_str + str(roles[i])

    try:
        banner_url = fetched_user.banner.url
    except:
        pass

    if status == discord.enums.Status(value="dnd"):
        status = "⛔ Do not disturb"

    elif status == discord.enums.Status(value="online"):
        status = "🟢 Online"

    elif status == discord.enums.Status(value="idle"):
        status = "🟡 Idle"

    else:
        status = "⚫ Offline"

    embed = discord.Embed(
        title=f"{name}'s Profile",
        description="Users public discord information, please don't use for bad or illegal purposes!",
    )
    embed.add_field(name="Display Name", value=name, inline=True)
    embed.add_field(name="Username", value=username, inline=True)
    embed.add_field(name="User ID", value=user_id, inline=True)
    embed.add_field(name="Creation Time", value=creation, inline=True)
    embed.add_field(name="Status", value=status, inline=True)
    embed.add_field(name="Badges", value=badges, inline=True)
    embed.add_field(name="Top role", value=top_role, inline=True)
    embed.add_field(
        name="Roles",
        value=("No roles" if roles_str.strip() == "" else roles_str),
        inline=True,
    )
    embed.set_thumbnail(
        url=(
            avatar
            if avatar
            else "https://i.pinimg.com/474x/d6/c1/09/d6c109542c43e5b7c6699761c8c78d16.jpg"
        )
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    embed.set_image(url=(banner_url if banner_url != None else ""))
    embed.color = color_manager.get_color("Blue")

    await message.channel.send(embed=embed)


async def nick_command(message: discord.Message):
    if (
        not message.author.guild_permissions.administrator
        | message.author.guild_permissions.administrator
    ):
        embed = discord.Embed(
            title="Missing permission",
            description=f"Missing required permission `manage_nicknames`. Please run `{BOT_PREFIX}help` for more information!",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}nick @user [new_nickname]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    user = message.mentions[0]

    if user not in message.guild.members:
        embed = discord.Embed(
            title="Member not in guild!",
            description=f"Please make sure that the user you are searching for exists and is in this guild. Usage: {BOT_PREFIX}nick @user [new_nick]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    args = message.content.split(" ")

    try:
        await user.edit(nick=" ".join(args[2:]))
        embed = discord.Embed(
            title="Successfully updated nickname!",
            description=f"Successfully updated nickname of <@{user.id}> to {" ".join(args[2:])}",
            color=color_manager.get_color("Green"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    except Exception as e:
        embed = discord.Embed(
            title="Issue occurred",
            description=f"An issue occurred during this operation. This exception was caught by a general handler. {e}",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return


async def feedback_command(message: discord.Message):
    args = message.content.split()[1:]
    feedback_text = " ".join(args)

    if len(args) < 1:
        embed = discord.Embed(
            title="Invalid Usage",
            description=f"Usage: {BOT_PREFIX}feedback [message]",
            color=color_manager.get_color("Red"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )
        await message.channel.send(embed=embed)
        return

    feedback.add_feedback(message.author.id, feedback_text)

    embed = discord.Embed(
        color=color_manager.get_color("Green"),
        title="Recorded Feedback",
        description=f"Recorded feedback from <@{message.author.id}>",
    )
    embed.add_field(name="Message", value=feedback_text, inline=False)
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)


async def restart_command(message: discord.Message):
    embed = discord.Embed(
        title="Warning",
        description=f"WARNING! This is a dev/debug command and will not be included in full release v1.0.0",
        color=color_manager.get_color("Orange"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)

    embed = discord.Embed(
        title="Restarting",
        description=f"The restart will take approximately 10 to 30 seconds on average.",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await message.channel.send(embed=embed)
    await client.close()
    os.execv(sys.executable, ["python"] + sys.argv)


async def translate_command(message: discord.Message):
    translate_text = message.content.split(" ", 1)[1]

    try:
        translator = GoogleTranslator(source="auto", target="en")
        translated_text = translator.translate(translate_text)

        embed = discord.Embed(
            title="Translation",
            description=translated_text,
            color=color_manager.get_color("Green"),
        )
        embed.set_footer(
            text=FOOTER_TEXT,
            icon_url=FOOTER_ICON,
        )

        await message.channel.send(embed=embed)

    except Exception as e:
        await message.channel.send(f"An error occurred: {str(e)}")


async def ping_command(message: discord.Message):
    bot_latency = round(client.latency * 1000)

    embed = discord.Embed(
        title="Bot latency",
        description=f"The current bot latency is approximately `{bot_latency}ms`",
        color=color_manager.get_color("Green"),
    )
    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )

    await message.channel.send(embed=embed)


@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return

    channel = client.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    embed = discord.Embed(
        title="Message Deleted", color=color_manager.get_color("Red"), timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Author", value=message.author.mention)
    embed.add_field(name="Channel", value=message.channel.mention)
    embed.add_field(name="Content", value=message.content or "No content")

    if message.attachments:
        embed.add_field(
            name="Attachments", value="\n".join([a.url for a in message.attachments])
        )

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=embed)


@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if before.author == client.user:
        return

    channel = client.get_channel(LOGGING_CHANNEL_ID)
    if not channel:
        return

    if before.content == after.content:
        return

    embed = discord.Embed(
        title="Message Edited", color=color_manager.get_color("Orange"), timestamp=datetime.datetime.utcnow()
    )
    embed.add_field(name="Author", value=before.author.mention)
    embed.add_field(name="Channel", value=before.channel.mention)
    embed.add_field(name="Before", value=before.content or "No content")
    embed.add_field(name="After", value=after.content or "No content")

    embed.set_footer(
        text=FOOTER_TEXT,
        icon_url=FOOTER_ICON,
    )
    await channel.send(embed=embed)
```

# src\cogs\ban.py

```py

```

# src\cogs\charinfo.py

```py

```

# src\cogs\feedback.py

```py

```

# src\cogs\help.py

```py
import discord

async def help_command(message: discord.Message, bot_prefix, bot_name, bot_version, footer_text, footer_icon, color_manager):
    embed = discord.Embed(
        title=f"{bot_name} v{bot_version} Help Information",
        description=f"Here are the available commands (prefix: {bot_prefix}):",
        color=color_manager.get_color("Blue"),
    )
    embed.set_footer(
        text=footer_text,
        icon_url=footer_icon,
    )

    commands = {
        "help": {"desc": "Show this help message", "usage": f"{bot_prefix}help"},
        "charinfo": {
            "desc": "Shows information and a image of the character provided",
            "usage": f"{bot_prefix}charinfo [character]",
        },
        "tts": {
            "desc": "Join the vc you are in and uses Text-to-Speech to say your text",
            "usage": f"{bot_prefix}tts [input_text]",
        },
        "nick": {
            "desc": "Changes guild specific username of a member (Mod only)",
            "usage": f"{bot_prefix}nick @user [new_nick]",
        },
        "feedback": {
            "desc": "Adds your feedback to our database",
            "usage": f"{bot_prefix}feedback [message]",
        },
        "play": {
            "desc": "Plays a song in the voice channel you are in",
            "usage": f"{bot_prefix}play [youtube_url]",
        },
        "profile": {
            "desc": "Gets information about the user.",
            "usage": f"{bot_prefix}profile @user",
        },
        "ping": {
            "desc": "Gets the ping (latency) of the Discord Bot",
            "usage": f"{bot_prefix}ping",
        },
        "translate": {
            "desc": "Translates the provided text to english",
            "usage": f"{bot_prefix}translate [text]",
        },
        "timeout": {
            "desc": "Timeout a user for a specified duration (Mod only)",
            "usage": f"{bot_prefix}timeout @user <duration> <unit> [reason]",
        },
        "kick": {
            "desc": "Kick a user from the server (Mod only)",
            "usage": f"{bot_prefix}kick @user [reason]",
        },
        "ban": {
            "desc": "Ban a user from the server (Admin only)",
            "usage": f"{bot_prefix}ban @user [reason]",
        },
        "unban": {
            "desc": "Unbans a user from the server (Admin only)",
            "usage": f"{bot_prefix}unban @user",
        },
        "shutdown": {
            "desc": "Shut down the bot (Admin only)",
            "usage": f"{bot_prefix}shutdown",
        },
        "start": {"desc": "Start the bot (Admin only)", "usage": f"{bot_prefix}start"},
    }

    for cmd, info in commands.items():
        embed.add_field(
            name=f"{bot_prefix}{cmd}",
            value=f"{info['desc']}\nUsage: `{info['usage']}`",
            inline=False,
        )

    embed.set_footer(
        text=footer_text,
        icon_url=footer_icon,
    )
    await message.channel.send(embed=embed)
```

# src\cogs\kick.py

```py

```

# src\cogs\nick.py

```py

```

# src\cogs\ping.py

```py

```

# src\cogs\play.py

```py

```

# src\cogs\profile.py

```py

```

# src\cogs\timeout.py

```py

```

# src\cogs\translate.py

```py
1
```

# src\cogs\tts.py

```py

```

# src\cogs\unban.py

```py

```

# src\utils\__init__.py

```py
print("Dont tell me what to do daddy! uwu ^_^")
```

# src\utils\helpers.py

```py
import datetime
import json
import tempfile
from collections import Counter

import discord
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from rich import print as richPrint
from langdetect import detect

def load_config(config_path: str) -> dict:
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default_prefix": "?", "guilds": {}}


def save_config(config: dict, CONFIG_PATH) -> None:
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)


def log_info(value: str) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(timestamp, end=" ")
    richPrint(f"[bold][blue]INFO[/blue][/bold] {value}")


class ColorManager:
    def __init__(self, config: dict):
        self.colors = config.get("colors", {})

    def get_color(self, color_name: str) -> int:
        if color_name not in self.colors:
            raise ValueError(f"Color '{color_name}' not found in configuration")
        return int(self.colors[color_name].lstrip("#"), 16)

    def list_colors(self) -> list:
        return list(self.colors.keys())

    def create_color_embed(
        self, title: str, description: str, color_name: str
    ) -> discord.Embed:
        color = self.get_color(color_name)
        return discord.Embed(title=title, description=description, color=color)


async def get_info_text(BOT_NAME, BOT_VERSION, BOT_PREFIX, CLIENT_USERNAME, CLIENT_USER_ID, LATENCY, GUILDS: int):
    return f"""
    {BOT_NAME} v{BOT_VERSION}
    Logged in as {CLIENT_USERNAME} (ID: {CLIENT_USER_ID})
    Connected to {GUILDS} guilds
    Bot is ready to use. Ping: {LATENCY}ms
    Prefix: {BOT_PREFIX}
    Initialization complete.
    """


def get_char_image(
    char: str, bg: str = "white", fg: str = "black", format: str = "png"
):
    try:
        img = Image.new("RGB", (200, 200), color=bg)
        d = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except IOError:
            font = ImageFont.load_default()

        d.text((100, 100), char, font=font, fill=fg, anchor="mm")

        with tempfile.NamedTemporaryFile(
            delete=False, suffix=f".{format}"
        ) as temp_file:
            img.save(temp_file, format=format.upper())
            temp_file_path = temp_file.name

        return temp_file_path
    except Exception as e:
        return None


def text_to_speech(text, output_file, tts_mode):
    try:
        if tts_mode == "slow":
            slow = True
        else:
            slow = False

        language = detect(text)
        tts = gTTS(text=text, lang=language, slow=slow)
        tts.save(output_file)

    except Exception as e:
        richPrint("ERROR_LOG ~ e:", e)


def detect_language(text):
    detections = [detect(text) for _ in range(5)]
    most_common = Counter(detections).most_common(1)[0][0]
    return most_common
```

# temp\audio\456935322370.mp3

This is a binary file of the type: Binary

