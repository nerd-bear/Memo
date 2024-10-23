# 404.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found | CRAC Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    
    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
</head>
<body class="bg-gray-100 text-gray-800 flex flex-col min-h-screen">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="flex-grow flex items-center justify-center px-4">
        <div class="text-center">
            <h1 class="text-6xl font-bold text-blue-600 mb-4">404</h1>
            <p class="text-2xl mb-8">Oops! Page not found</p>
            <p class="text-xl mb-8">It seems like CRAC Bot couldn't find the page you're looking for.</p>
            <div class="flex justify-center space-x-4">
                <a href="https://crac.nerd-bear.org/" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-150 ease-in-out transform hover:scale-105">
                    Return to Homepage
                </a>
                <button onclick="location.reload()" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-150 ease-in-out transform hover:scale-105">
                    Reload Page
                </button>
            </div>
        </div>
    </main>
    
    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('h1', {duration: 1, y: -50, opacity: 0, ease: 'bounce'});
            gsap.from('p', {duration: 1, y: 50, opacity: 0, stagger: 0.2});
            gsap.from('a, button', {duration: 1, opacity: 100, y: 20, delay: 1, stagger: 0.2});
        });
    </script>
</body>
</html>
```

# articles\add-feedback.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Feedback Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Feedback Guide">
    <meta property="og:description" content="Learn how to submit feedback for CRAC Bot using the feedback command. Your input helps improve the bot!">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/add-feedback">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">Submitting Feedback for CRAC Bot</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-10-17">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>3 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">The Importance of Your Feedback</h3>
                    <p class="mb-4">Your feedback is crucial for the continuous improvement of CRAC Bot. Whether you've encountered a bug, have a feature request, or simply want to share your thoughts, we want to hear from you! The feedback command makes it easy to submit your input directly through Discord.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Using the Feedback Command</h4>
                    <p class="mb-4">Submitting feedback is straightforward with the <code class="bg-gray-100 p-1 rounded">?feedback</code> command. Here's how to use it:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?feedback [your message]</pre>
                    <p>Replace [your message] with your actual feedback. Be as detailed as possible to help us understand your thoughts or the issue you're experiencing.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Examples of Good Feedback</h4>
                    <p class="mb-4">Here are some examples of effective feedback submissions:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><code class="bg-gray-100 p-1 rounded">?feedback The ?play command sometimes fails to join the voice channel. Could you look into this?</code></li>
                        <li><code class="bg-gray-100 p-1 rounded">?feedback I love the ?profile command! It would be great if it could also show the user's top 3 most active channels.</code></li>
                        <li><code class="bg-gray-100 p-1 rounded">?feedback The bot seems to lag when processing commands in servers with over 1000 members. Any way to optimize this?</code></li>
                    </ul>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">What Happens After You Submit Feedback</h4>
                    <p class="mb-4">After submitting your feedback:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Your feedback is securely stored in our database.</li>
                        <li>The development team regularly reviews all feedback submissions.</li>
                        <li>Your input may influence future updates and improvements to CRAC Bot.</li>
                        <li>For urgent issues, consider also reaching out through our support channels.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Best Practices for Submitting Feedback</h3>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Be specific: Provide as much detail as possible about your experience or suggestion.</li>
                        <li>One idea per submission: If you have multiple suggestions, submit them separately for easier processing.</li>
                        <li>Be constructive: Explain not just what you dislike, but how you think it could be improved.</li>
                        <li>Include context: Mention your server size, the command you were using, or any relevant settings.</li>
                    </ul>

                    <p class="text-lg font-semibold mt-8">Your feedback plays a vital role in shaping the future of CRAC Bot. We appreciate every submission and take your input seriously in our development process.</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>If you're reporting a bug, try to include steps to reproduce the issue. This helps our development team identify and fix the problem more quickly!</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# articles\articles.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Articles</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Articles">
    <meta property="og:description" content="Explore all articles about CRAC Bot, including guides on commands, configuration, and feedback submission.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/articles">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/articles" class="hover:text-blue-600 transition">Articles</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <h2 class="text-4xl font-bold mb-8 text-center">CRAC Bot Articles</h2>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <!-- Config Guide Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Configuration Guide</h3>
                    <p class="text-gray-600 mb-4">Learn how to configure CRAC Bot for your server's needs.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">5 min read</span>
                    </div>
                    <a href="/support/article/config-guide" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>

            <!-- Commands Guide Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Commands Guide</h3>
                    <p class="text-gray-600 mb-4">Explore all available commands and how to use them effectively.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">8 min read</span>
                    </div>
                    <a href="/support/article/commands-guide" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>

            <!-- Feedback Submission Article -->
            <div class="bg-white rounded-lg shadow-md overflow-hidden">
                <div class="p-6">
                    <h3 class="text-xl font-bold mb-2">Submitting Feedback</h3>
                    <p class="text-gray-600 mb-4">Learn how to submit feedback to help improve CRAC Bot.</p>
                    <div class="flex items-center justify-between mt-4">
                        <div class="flex items-center">
                            <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-8 h-8 rounded-full mr-2">
                            <span class="text-sm text-gray-600">Nerd Bear</span>
                        </div>
                        <span class="text-sm text-gray-500">3 min read</span>
                    </div>
                    <a href="/support/article/add-feedback" class="mt-4 inline-block text-blue-600 hover:text-blue-800">Read More →</a>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('.grid > div', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                stagger: 0.2,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# articles\commands-guide.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Commands Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Commands Guide">
    <meta property="og:description" content="Learn how to use CRAC Bot's commands effectively for server management and user interaction.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/commands-guide">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">CRAC Bot Commands Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-10-17">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>4 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Getting Started with CRAC Bot Commands</h3>
                    <p class="mb-4">CRAC Bot comes packed with a variety of commands to help you manage your server and engage with your community. In this guide, we'll walk you through the most important commands and how to use them effectively.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Basic Command Structure</h4>
                    <p class="mb-4">All CRAC Bot commands start with a prefix. By default, this prefix is set to "?", but it can be customized in the config file. Here's the basic structure of a command:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?commandName [argument1] [argument2] ...</pre>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Essential Commands</h3>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">1. Help Command</h4>
                    <p class="mb-4">The help command is your go-to for information about all available commands:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">?help</pre>
                    <p>This will display a list of all available commands along with a brief description of each.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">2. Moderation Commands</h4>
                    <p class="mb-4">CRAC Bot offers several moderation commands to help you manage your server:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Kick:</strong> ?kick @user [reason]</li>
                        <li><strong>Ban:</strong> ?ban @user [reason]</li>
                        <li><strong>Unban:</strong> ?unban @user</li>
                        <li><strong>Timeout:</strong> ?timeout @user &lt;duration&gt; &lt;unit&gt; [reason]</li>
                    </ul>
                    <p>Remember, you need the appropriate permissions to use these commands.</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">3. Fun and Utility Commands</h4>
                    <p class="mb-4">CRAC Bot also includes commands for entertainment and utility:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Character Info:</strong> ?charinfo [character]</li>
                        <li><strong>Text-to-Speech:</strong> ?tts [message]</li>
                        <li><strong>Play Music:</strong> ?play [youtube_url]</li>
                        <li><strong>User Profile:</strong> ?profile @user</li>
                    </ul>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">4. Bot Management Commands</h4>
                    <p class="mb-4">For server administrators, there are commands to manage the bot itself:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>Shutdown:</strong> ?shutdown</li>
                        <li><strong>Start:</strong> ?start</li>
                        <li><strong>Change Nickname:</strong> ?nick @user [new_nickname]</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Advanced Usage Tips</h3>
                    <p class="mb-4">Here are some tips to help you get the most out of CRAC Bot:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Use the ?help command followed by a specific command name for detailed usage information.</li>
                        <li>When using moderation commands, always provide a reason to maintain transparency.</li>
                        <li>The ?tts command is great for making announcements in voice channels.</li>
                        <li>Use ?profile to quickly get information about a user, including their roles and join date.</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Troubleshooting Common Issues</h3>
                    <p class="mb-4">If you're experiencing issues with commands, try these steps:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Ensure you're using the correct prefix (default is "?").</li>
                        <li>Check that you have the necessary permissions for the command.</li>
                        <li>Verify that the bot is online and has the required permissions in your server.</li>
                        <li>If a command isn't working, try restarting the bot using the ?shutdown and ?start commands (admin only).</li>
                    </ol>

                    <p class="text-lg font-semibold mt-8">Remember, the key to effectively using CRAC Bot is experimentation. Don't be afraid to try out different commands and see how they can benefit your server!</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>Create a dedicated channel for bot commands to keep your main chat channels clutter-free. This also helps new users learn how to interact with the bot by seeing others use it.</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# articles\config-guide.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Config Guide</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>
    
    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Config Guide">
    <meta property="og:description" content="Learn how to change and use the config file for CRAC Bot, a versatile Discord bot for server management and user interaction.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support/article/config-guide">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <article class="bg-white rounded-lg shadow-md overflow-hidden">
            <div class="relative">
                <div class="absolute inset-0 bg-black opacity-50"></div>
                <div class="absolute inset-0 flex items-center justify-center">
                    <h2 class="text-4xl font-bold text-black mt-20">CRAC Bot Config Guide</h2>
                </div>
            </div>
            
            <div class="p-8">
                <div class="flex items-center mb-6">
                    <img src="https://nerd-bear.org/favicon.ico" alt="Author Avatar" class="w-12 h-12 rounded-full mr-4">
                    <div>
                        <p class="font-bold">Nerd Bear</p>
                        <p class="text-gray-600 text-sm">CRAC Bot Developer</p>
                    </div>
                </div>
                
                <div class="flex items-center text-gray-600 text-sm mb-6">
                    <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    <time datetime="2024-05-15">October 17, 2024</time>
                    <span class="mx-2">•</span>
                    <span>5 min read</span>
                </div>

                <div class="prose max-w-none">
                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Understanding the Config File</h3>
                    <p class="mb-4">The config file for CRAC Bot is a JSON file named <code class="bg-gray-100 p-1 rounded">config.json</code>. It contains various settings that control the bot's behavior. Let's dive into its structure and how you can customize it to suit your needs.</p>

                    <pre class="bg-gray-100 p-4 rounded-md mb-4 overflow-x-auto">
{
    "defaults": {
        "prefix": "?",
        "footer_text": "This bot is created and hosted by Nerd bear",
        "footer_icon": "https://as2.ftcdn.net/v2/jpg/01/17/00/87/1000_F_117008730_0Dg5yniuxPQLz3shrJvLIeBsPfPRBSE1.jpg"
    },
    "bot_version": "0.4.6",
    "bot_name": "CRAC",
    "tts_mode": "fast",
    "log_channel_id": "1290060885485948950",
    "tts_detector_factory_seed": "0",
    "colors": {
        "Red": "#FFB3BA",
        "Blue": "#B5DEFF"
        // ... other colors ...
    },
    "guilds": {
        "1288144110880030795": {
            "prefix": "*"
        }
    }
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Key Sections:</h4>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li><strong>defaults:</strong> Contains default settings for the bot.</li>
                        <li><strong>bot_version:</strong> The current version of the bot.</li>
                        <li><strong>bot_name:</strong> The name of the bot.</li>
                        <li><strong>tts_mode:</strong> The mode for text-to-speech functionality.</li>
                        <li><strong>log_channel_id:</strong> The ID of the channel where logs will be sent.</li>
                        <li><strong>colors:</strong> A list of color codes used for various bot functions.</li>
                        <li><strong>guilds:</strong> Server-specific settings, such as custom prefixes.</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">How to Modify the Config File</h3>
                    <p class="mb-4">Customizing your CRAC Bot installation is straightforward. Follow these steps to modify the config file:</p>
                    <ol class="list-decimal list-inside mb-4 space-y-2">
                        <li>Locate the <code class="bg-gray-100 p-1 rounded">config.json</code> file in your bot's root directory.</li>
                        <li>Open the file with a text editor (e.g., Notepad++, Visual Studio Code).</li>
                        <li>Make your desired changes, ensuring to maintain the correct JSON format.</li>
                        <li>Save the file after making changes.</li>
                        <li>Restart the bot for the changes to take effect.</li>
                    </ol>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Common Modifications</h3>
                    <p class="mb-4">Let's explore some common modifications you might want to make to your CRAC Bot configuration:</p>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Changing the Default Prefix</h4>
                    <p class="mb-4">To change the default prefix, modify the "prefix" value under "defaults":</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"defaults": {
    "prefix": "!",  // Change '?' to your desired prefix
    ...
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Setting a Custom Prefix for a Specific Server</h4>
                    <p class="mb-4">To set a custom prefix for a specific server, add or modify an entry under "guilds":</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"guilds": {
    "YOUR_SERVER_ID": {
        "prefix": "$"  // Replace with your desired prefix
    }
}
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Changing the Bot Name</h4>
                    <p class="mb-4">To change the bot's name, modify the "bot_name" value:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"bot_name": "Your New Bot Name",
                    </pre>

                    <h4 class="text-xl font-bold mb-2 text-blue-600">Modifying Colors</h4>
                    <p class="mb-4">To change or add colors, modify the "colors" section:</p>
                    <pre class="bg-gray-100 p-4 rounded-md mb-4">
"colors": {
    "Red": "#FF0000",
    "Blue": "#0000FF",
    "CustomColor": "#HEXCODE"
}
                    </pre>

                    <h3 class="text-2xl font-bold mb-4 text-blue-600">Important Notes</h3>
                    <p class="mb-4">Before you start tweaking your config file, keep these important points in mind:</p>
                    <ul class="list-disc list-inside mb-4 space-y-2">
                        <li>Always backup your config file before making changes.</li>
                        <li>Ensure your JSON syntax is correct to avoid errors.</li>
                        <li>Some changes may require a bot restart to take effect.</li>
                        <li>Be cautious when changing critical settings like log_channel_id.</li>
                    </ul>

                    <p class="text-lg font-semibold mt-8">Remember, customizing your CRAC Bot is all about making it work best for your server and community. Don't be afraid to experiment with different settings to find what works best for you!</p>

                    <div class="mt-8 p-4 bg-blue-100 rounded-md">
                        <p class="font-bold text-blue-800">Pro Tip:</p>
                        <p>Consider using a JSON validator tool to check your config file for syntax errors before restarting your bot. This can save you time and prevent potential issues.</p>
                    </div>
                </div>
            </div>
        </article>

        <div class="mt-8">
            <h3 class="text-2xl font-bold mb-4">Comments</h3>
            <p>No comments could be found for this article</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('article', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# commands\ban\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Ban Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Ban Command">
    <meta property="og:description" content="Learn how to use the ban command in CRAC Bot to moderate your server.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/ban">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Ban Command</h1>
            <p class="text-xl text-gray-600">Permanently remove a user from your server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?ban @user [reason]
                    </div>
                    <p class="mb-4">The ban command allows moderators to permanently remove a user from the server. The user cannot rejoin unless unbanned.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to ban (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the ban</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic ban:</p>
                            <pre class="bg-gray-50 rounded p-4">?ban @UserName</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Ban with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?ban @UserName 7 Repeated violations of server rules</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Banned</p>
                                    <p class="text-gray-600">@UserName has been banned.</p>
                                    <p class="text-gray-600">Reason: Repeated violations of server rules</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Ban Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>The bot must have a role higher than the banned user</li>
                        <li>Banned users cannot rejoin with invites</li>
                        <li>The bot will attempt to DM the user the reason for their ban</li>
                        <li>Server owner cannot be banned</li>
                        <li>Ban is logged in the server's audit log</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\charinfo\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Character Info Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Character Info Command">
    <meta property="og:description" content="Get detailed information about any character using CRAC Bot's charinfo command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/charinfo">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Character Info Command</h1>
            <p class="text-xl text-gray-600">Get detailed Unicode information about any character</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?charinfo [character]
                    </div>
                    <p class="mb-4">The charinfo command provides detailed Unicode information about any character, including emojis, special characters, and letters.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">character</code> - The character you want to analyze</li>
                        </ul>
                    </div>
                </section>

                <!-- Information Provided Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Information Provided</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Original character</li>
                                <li>Character name</li>
                                <li>Character category</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Unicode Data:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Unicode value (U+XXXX)</li>
                                <li>Unicode escape sequence</li>
                                <li>Full Unicode escape</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Additional Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Python escape sequence</li>
                                <li>Character preview</li>
                                <li>Visual representation</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get info about an emoji:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo 😀</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Get info about a special character:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo ♠</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Get info about a letter:</p>
                            <pre class="bg-gray-50 rounded p-4">?charinfo A</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Character info</p>
                                    <p class="text-gray-600">Information on character: A</p>
                                    <p class="text-gray-600">Original character: A</p>
                                    <p class="text-gray-600">Character name: LATIN CAPITAL LETTER A</p>
                                    <p class="text-gray-600">Character category: Lu</p>
                                    <p class="text-gray-600">Unicode value: U+0041</p>
                                    <p class="text-gray-600">Unicode escape: \u0041</p>
                                    <p class="text-gray-600">Full Unicode escape: \U00000041</p>
                                    <p class="text-gray-600">Python escape: 'A'</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">ERROR</p>
                                    <p class="text-red-600">Please provide a character to get information about.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Supported Characters</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Standard letters</li>
                        <li>Numbers</li>
                        <li>Emojis</li>
                        <li>Special symbols</li>
                        <li>Unicode characters</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Uses</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Finding Unicode values</li>
                        <li>Getting character names</li>
                        <li>Learning character categories</li>
                        <li>Getting escape sequences</li>
                        <li>Character analysis</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\coin\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Coin Flip Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Coin Flip Command">
    <meta property="og:description" content="Flip a virtual coin using CRAC Bot's coin command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/coin">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Coin Flip Command</h1>
            <p class="text-xl text-gray-600">Flip a virtual coin and get heads or tails</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?coin
                    </div>
                    <p class="mb-4">The coin command flips a virtual coin and displays the result. The bot will first announce it's flipping the coin, then show whether it landed on heads or tails.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?coin</li>
                        </ul>
                    </div>
                </section>

                <!-- How It Works Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">How It Works</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-4">The coin flip happens in two steps:</p>
                            <ol class="list-decimal list-inside space-y-2">
                                <li class="p-2">Bot announces "Flipping a coin..."</li>
                                <li class="p-2">Result is shown: "The coin landed on heads/tails!"</li>
                            </ol>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Flip a coin:</p>
                            <pre class="bg-gray-50 rounded p-4">?coin</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="text-gray-600">Flipping a coin...</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">The coin landed on heads! 🪙</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Possible Results</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Heads</li>
                        <li>Tails</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Making random decisions</li>
                        <li>Settling debates</li>
                        <li>Simple games</li>
                        <li>Quick choices</li>
                        <li>Team selection</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Results are random</li>
                        <li>50/50 probability</li>
                        <li>Shows flipping animation</li>
                        <li>Works in any channel</li>
                        <li>Instant results</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\feedback\index.html

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRAC Bot - Feedback Command</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

        <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
        
        <meta property="og:title" content="CRAC Bot | Feedback Command">
        <meta property="og:description" content="Learn how to submit feedback to help improve CRAC Bot.">
        <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
        <meta property="og:url" content="https://crac.nerd-bear.org/commands/feedback">
        <meta property="og:type" content="website">

        <style>
            .pfp-hover {
                transition: transform 0.3s ease-in-out;
            }
            .pfp-hover:hover {
                transform: scale(1.1);
            }
            pre {
                white-space: pre-wrap;
                word-wrap: break-word;
            }
        </style>
    </head>
    <body class="bg-gray-50 text-gray-800">
        <nav class="container mx-auto p-6">
            <div class="flex justify-between items-center">
                <h1 class="text-3xl font-bold text-blue-600">
                    <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
                </h1>
                <ul class="flex space-x-6">
                    <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                    <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                    <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                    <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                </ul>
            </div>
        </nav>

        <main class="container mx-auto mt-12 p-6">
            <!-- Command Header -->
            <div class="mb-8">
                <div class="flex items-center gap-4 mb-4">
                    <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                    <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                </div>
                <h1 class="text-4xl font-bold mb-2">Feedback Command</h1>
                <p class="text-xl text-gray-600">Submit feedback to help improve CRAC Bot</p>
            </div>

            <!-- Command Card Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Main Content -->
                <div class="md:col-span-2 space-y-8">
                    <!-- Usage Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Usage</h2>
                        <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                            ?feedback [message]
                        </div>
                        <p class="mb-4">The feedback command allows you to submit suggestions, bug reports, or general feedback about CRAC Bot. All feedback is stored and reviewed regularly by the development team.</p>
                        <div class="space-y-2">
                            <p><strong>Arguments:</strong></p>
                            <ul class="list-disc list-inside pl-4">
                                <li><code class="bg-gray-100 px-1 rounded">message</code> - Your feedback message</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Best Practices Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Feedback Best Practices</h2>
                        <div class="space-y-4">
                            <div class="p-4 bg-gray-50 rounded">
                                <p class="font-bold mb-2">Good Feedback Examples:</p>
                                <ul class="list-disc list-inside text-gray-600">
                                    <li>Bug reports with steps to reproduce</li>
                                    <li>Specific feature requests</li>
                                    <li>Detailed improvement suggestions</li>
                                    <li>Command enhancement ideas</li>
                                </ul>
                            </div>
                            <div class="p-4 bg-yellow-50 rounded">
                                <p class="font-bold text-yellow-800 mb-2">Avoid:</p>
                                <ul class="list-disc list-inside text-yellow-700">
                                    <li>Abuse or harassment</li>
                                    <li>Spam submissions</li>
                                    <li>Very short/vague feedback</li>
                                    <li>Support requests (use ?help instead)</li>
                                </ul>
                            </div>
                        </div>
                    </section>

                    <!-- Examples Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Examples</h2>
                        <div class="space-y-4">
                            <div>
                                <p class="font-medium mb-2">Bug report:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback The ?play command sometimes fails to join voice channels in servers with over 1000 members</pre>
                            </div>
                            <div>
                                <p class="font-medium mb-2">Feature request:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback Would be great to have a queue system for the music commands</pre>
                            </div>
                            <div>
                                <p class="font-medium mb-2">General feedback:</p>
                                <pre class="bg-gray-50 rounded p-4">?feedback Love the profile command! Maybe add an option to show favorite channels?</pre>
                            </div>
                        </div>
                    </section>

                    <!-- Response Section -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                        <div class="space-y-4">
                            <div class="border rounded p-4">
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                    <span class="font-medium">CRAC Bot</span>
                                </div>
                                <div class="pl-10">
                                    <div class="bg-gray-50 rounded p-4">
                                        <p class="font-medium">Feedback Received</p>
                                        <p class="text-gray-600">Thank you for your feedback! Your message has been stored and will be reviewed by our team.</p>
                                    </div>
                                </div>
                            </div>
                            <div class="border rounded p-4 border-red-200">
                                <div class="flex items-center gap-2 mb-2">
                                    <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                    <span class="font-medium">CRAC Bot</span>
                                </div>
                                <div class="pl-10">
                                    <div class="bg-red-50 rounded p-4">
                                        <p class="font-medium text-red-800">Error</p>
                                        <p class="text-red-600">Please provide a feedback message. Usage: ?feedback [message]</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>

                <!-- Sidebar -->
                <div class="space-y-6">
                    <!-- Required Permissions -->
                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                        <ul class="space-y-2 text-gray-600">
                            <li class="flex items-center gap-2">
                                <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                None required
                            </li>
                        </ul>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                        <p class="text-gray-600">No cooldown</p>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">What Happens Next?</h3>
                        <ul class="space-y-2 text-gray-600 list-disc list-inside">
                            <li>Feedback is securely stored</li>
                            <li>Reviewed by development team</li>
                            <li>Used to guide improvements</li>
                            <li>May influence future updates</li>
                        </ul>
                    </section>

                    <section class="bg-white rounded-lg shadow-sm p-6">
                        <h3 class="text-xl font-bold mb-4">Tips for Good Feedback</h3>
                        <ul class="space-y-2 text-gray-600 list-disc list-inside">
                            <li>Be specific and detailed</li>
                            <li>One idea per submission</li>
                            <li>Include examples if possible</li>
                            <li>Explain why it matters</li>
                            <li>Be constructive</li>
                        </ul>
                    </section>
                </div>
            </div>
        </main>

        <footer class="bg-gray-100 mt-24 py-8">
            <div class="container mx-auto text-center text-gray-600">
                <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
                <div class="mt-4">
                    <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                    <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                    <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
                </div>
            </div>
        </footer>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                gsap.from('main > *', {
                    duration: 0.5,
                    opacity: 0,
                    y: 20,
                    stagger: 0.1,
                    ease: 'power2.out'
                });
            });
        </script>
    </body>
    </html>
```

# commands\help\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Help Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Help Command">
    <meta property="og:description" content="Learn how to use the help command in CRAC Bot to learn more about the commands you can use.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/help">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Help Command</h1>
            <p class="text-xl text-gray-600">Display a list of all available commands.</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?help
                    </div>
                    <p class="mb-4">The help command shows you a large embed of all the commands that you can run in the guild along with their short description.</p>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Help:</p>
                            <pre class="bg-gray-50 rounded p-4">?help</pre>
                        </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">CRAC Help Information</p>
                                    <p class="text-gray-600">?tts</p>
                                    <p class="text-gray-600 font-bold">Join the vc you are in and uses Text-to-Speech to say your text<br/><code>Usage: ?tts [input_text]</code></p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/profile" class="text-blue-600 hover:text-blue-800">?profile</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/server" class="text-blue-600 hover:text-blue-800">?server</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/charinfo" class="text-blue-600 hover:text-blue-800">?charinfo</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>There are some commands that are marked as secret/easter egg commands and are not documented.</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Commands</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <meta property="og:title" content="CRAC Bot | Commands">
    <meta property="og:description" content="Explore all available commands for CRAC Bot, including moderation, music, utility, and fun features.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands">
    <meta property="og:type" content="website">

    <style>
        .command-card {
            transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
        .command-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>

<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-center text-gray-900">Command List</h2>
            <p class="text-xl text-gray-600 mb-8 text-center">Explore all available commands for CRAC Bot</p>
        </div>

        <div class="mb-8">
            <div class="flex flex-col md:flex-row gap-4">
                <input type="text" id="search-input" placeholder="Search commands..." class="flex-grow p-2 border border-gray-300 rounded-md">
                <select id="category-filter" class="p-2 border border-gray-300 rounded-md">
                    <option value="all">All Categories</option>
                    <option value="moderation">Moderation</option>
                    <option value="music">Music</option>
                    <option value="utility">Utility</option>
                    <option value="fun">Fun</option>
                </select>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4" id="commands-grid">
            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?kick</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Kick a user from the server with an optional reason.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/kick" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?ban</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Ban a user from the server with an optional reason.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/ban" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?unban</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Unban a previously banned user.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/unban" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?timeout</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Timeout a user for a specified duration.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/timeout" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="moderation">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?nick</h3>
                        <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
                    </div>
                    <p class="text-gray-600 text-sm">Change a user's nickname.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/nick" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?play</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Play a song from YouTube in your voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/play" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?join</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Make the bot join your voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/join" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="music">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?leave</h3>
                        <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
                    </div>
                    <p class="text-gray-600 text-sm">Make the bot leave the voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/leave" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?help</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Display a list of all available commands.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/help" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?profile</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">View detailed information about a user's profile.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/profile" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?feedback</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Submit feedback about the bot.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/feedback" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?translate</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Translate text to English from any language.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/translate" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?ping</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">Check the bot's current latency.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/ping" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="utility">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?server</h3>
                        <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
                    </div>
                    <p class="text-gray-600 text-sm">View detailed information about the server.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/server" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?charinfo</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get detailed information about a character or emoji.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/charinfo" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?tts</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Convert text to speech in a voice channel.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/tts" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?joke</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get a random dad joke.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/joke" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?coin</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Flip a coin and get heads or tails.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/coin" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>

            <div class="command-card bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col min-h-[200px]" data-category="fun">
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-lg font-semibold text-blue-600">?quote</h3>
                        <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
                    </div>
                    <p class="text-gray-600 text-sm">Get the quote of the day.</p>
                </div>
                <div class="mt-2 pt-2 border-t border-gray-100">
                    <a href="/commands/quote" class="text-blue-600 hover:text-blue-800 text-sm">Learn more →</a>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-2">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const categoryFilter = document.getElementById('category-filter');
            const commandCards = document.querySelectorAll('.command-card');

            function filterCommands() {
                const searchTerm = searchInput.value.toLowerCase();
                const selectedCategory = categoryFilter.value;

                commandCards.forEach(card => {
                    const commandText = card.textContent.toLowerCase();
                    const cardCategory = card.dataset.category;
                    const matchesSearch = commandText.includes(searchTerm);
                    const matchesCategory = selectedCategory === 'all' || cardCategory === selectedCategory;

                    if (matchesSearch && matchesCategory) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            }

            searchInput.addEventListener('input', filterCommands);
            categoryFilter.addEventListener('change', filterCommands);

            gsap.from('.command-card', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>

</html>
```

# commands\join\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Join Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Join Command">
    <meta property="og:description" content="Learn how to make CRAC Bot join your voice channel using the join command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/join">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Join Command</h1>
            <p class="text-xl text-gray-600">Make the bot join your current voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?join
                    </div>
                    <p class="mb-4">The join command makes CRAC Bot join your current voice channel. You must be in a voice channel for this command to work.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Bot joins your current voice channel</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic usage:</p>
                            <pre class="bg-gray-50 rounded p-4">?join</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Joined Voice Channel</p>
                                    <p class="text-gray-600">Successfully joined General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">You must be in a voice channel to use this command.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Voice Channel Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Voice Channel Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">For the command to work:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>You must be in a voice channel</li>
                                <li>The voice channel must be visible to the bot</li>
                                <li>The bot must have permission to join the channel</li>
                                <li>The voice channel must not be at capacity</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            View Channel
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/play" class="text-blue-600 hover:text-blue-800">?play</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>User not in a voice channel</li>
                        <li>Bot missing permissions</li>
                        <li>Voice channel at capacity</li>
                        <li>Region voice server issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot stays in channel until disconnected</li>
                        <li>Will automatically disconnect after inactivity</li>
                        <li>Can be used before playing music</li>
                        <li>Works in any accessible voice channel</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\joke\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Joke Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Joke Command">
    <meta property="og:description" content="Get a random dad joke using CRAC Bot's joke command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/joke">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Joke Command</h1>
            <p class="text-xl text-gray-600">Get a random dad joke to lighten the mood</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?joke
                    </div>
                    <p class="mb-4">The joke command returns a random dad joke. Each time you use the command, you'll get a different joke!</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?joke</li>
                        </ul>
                    </div>
                </section>

                <!-- Example Jokes Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example Jokes</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-2">Sample Responses:</p>
                            <ul class="space-y-4 text-gray-600">
                                <li class="p-2 bg-white rounded shadow-sm">"Why don't eggs tell jokes? They'd crack up!"</li>
                                <li class="p-2 bg-white rounded shadow-sm">"What do you call a fake noodle? An impasta!"</li>
                                <li class="p-2 bg-white rounded shadow-sm">"Why did the scarecrow win an award? He was outstanding in his field!"</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get a random joke:</p>
                            <pre class="bg-gray-50 rounded p-4">?joke</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Dad Joke Time! 😄</p>
                                    <p class="text-gray-600">Why don't eggs tell jokes?</p>
                                    <p class="text-gray-600">They'd crack up!</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Features</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Random selection</li>
                        <li>Family-friendly content</li>
                        <li>Classic dad humor</li>
                        <li>Different joke every time</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Breaking the ice</li>
                        <li>Lightening the mood</li>
                        <li>Starting conversations</li>
                        <li>Having a quick laugh</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>All jokes are dad jokes</li>
                        <li>Content is always clean</li>
                        <li>Jokes may repeat eventually</li>
                        <li>Works in any channel</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\kick\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Kick Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Kick Command">
    <meta property="og:description" content="Learn how to use the kick command in CRAC Bot to moderate your server.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/kick">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Kick Command</h1>
            <p class="text-xl text-gray-600">Remove a user from your server temporarily</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?kick @user [reason]
                    </div>
                    <p class="mb-4">The kick command allows moderators to remove a user from the server. The user can rejoin with a new invite.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to kick (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional reason for the kick</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic kick:</p>
                            <pre class="bg-gray-50 rounded p-4">?kick @UserName</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Kick with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?kick @UserName Spamming in general chat</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Kicked</p>
                                    <p class="text-gray-600">@UserName has been kicked.</p>
                                    <p class="text-gray-600">Reason: Spamming in general chat</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Kick Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>The bot must have a role higher than the kicked user</li>
                        <li>Kicked users can rejoin with a new invite</li>
                        <li>The bot will attempt to DM the user the reason for their kick</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\leave\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Leave Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Leave Command">
    <meta property="og:description" content="Learn how to make CRAC Bot leave your voice channel using the leave command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/leave">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Leave Command</h1>
            <p class="text-xl text-gray-600">Make the bot leave its current voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?leave
                    </div>
                    <p class="mb-4">The leave command makes CRAC Bot leave the voice channel it's currently in. The bot must be in a voice channel for this command to work.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Bot leaves its current voice channel</li>
                        </ul>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic usage:</p>
                            <pre class="bg-gray-50 rounded p-4">?leave</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Left Voice Channel</p>
                                    <p class="text-gray-600">Successfully left General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">I'm not in a voice channel.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Command Behavior Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Command Behavior</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">When using this command:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Bot will stop any currently playing audio</li>
                                <li>Bot will immediately disconnect from the voice channel</li>
                                <li>Command can be used by any member</li>
                                <li>No need to be in the same voice channel as the bot</li>
                            </ul>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/play" class="text-blue-600 hover:text-blue-800">?play</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot not in any voice channel</li>
                        <li>Bot temporarily unresponsive</li>
                        <li>Network connectivity issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Stops any playing audio</li>
                        <li>Can be used from any channel</li>
                        <li>Immediate disconnection</li>
                        <li>No confirmation needed</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\nick\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Nickname Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Nickname Command">
    <meta property="og:description" content="Learn how to use the nickname command in CRAC Bot to change user nicknames.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/nick">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Nickname Command</h1>
            <p class="text-xl text-gray-600">Change a user's nickname in the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?nick @user [new_nickname]
                    </div>
                    <p class="mb-4">The nickname command allows moderators to change a user's display name in the server. If no new nickname is provided, it will reset to their original username.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to rename (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">new_nickname</code> - Optional: New nickname for the user (omit to reset)</li>
                        </ul>
                    </div>
                </section>

                <!-- Nickname Rules Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Nickname Rules</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Length Requirements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Minimum: 1 character</li>
                                <li>Maximum: 32 characters</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Restrictions:</p>
                            <ul class="list-disc list-inside text-yellow-700">
                                <li>Cannot contain Discord's blocked words</li>
                                <li>Cannot contain server-specific blocked words</li>
                                <li>Cannot impersonate other users</li>
                                <li>Cannot use certain special characters</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Set new nickname:</p>
                            <pre class="bg-gray-50 rounded p-4">?nick @UserName Cool Person</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Reset nickname:</p>
                            <pre class="bg-gray-50 rounded p-4">?nick @UserName</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Nickname Changed</p>
                                    <p class="text-gray-600">Changed nickname for @UserName to "Cool Person"</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Cannot change nickname: Missing permissions or nickname invalid.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Manage Nicknames
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot must have a role higher than the user</li>
                        <li>Cannot change server owner's nickname</li>
                        <li>Changes are logged in the audit log</li>
                        <li>Users with "Change Nickname" permission can change their own nickname</li>
                        <li>Nickname changes are immediate</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Nickname too long (>32 characters)</li>
                        <li>Contains blocked words or characters</li>
                        <li>Bot role hierarchy insufficient</li>
                        <li>User has higher roles than bot</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\ping\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Ping Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Ping Command">
    <meta property="og:description" content="Check CRAC Bot's response time using the ping command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/ping">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Ping Command</h1>
            <p class="text-xl text-gray-600">Check the bot's current response time</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?ping
                    </div>
                    <p class="mb-4">The ping command shows the bot's current latency (response time) in milliseconds. This can help you check if the bot is experiencing any delays or connection issues.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?ping</li>
                        </ul>
                    </div>
                </section>

                <!-- Understanding Latency Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Understanding Latency</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-green-50 rounded">
                            <p class="font-bold text-green-800 mb-2">Good Latency:</p>
                            <p class="text-green-700">50-150ms</p>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Moderate Latency:</p>
                            <p class="text-yellow-700">150-300ms</p>
                        </div>
                        <div class="p-4 bg-red-50 rounded">
                            <p class="font-bold text-red-800 mb-2">High Latency:</p>
                            <p class="text-red-700">300ms+</p>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Check bot latency:</p>
                            <pre class="bg-gray-50 rounded p-4">?ping</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">🏓 Pong!</p>
                                    <p class="text-gray-600">Bot Latency: 87ms</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">When to Use</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Bot seems unresponsive</li>
                        <li>Commands are delayed</li>
                        <li>Checking connection quality</li>
                        <li>Troubleshooting issues</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Latency varies by region</li>
                        <li>Results may fluctuate</li>
                        <li>Lower is better</li>
                        <li>Simple health check tool</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\play\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Play Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Play Command">
    <meta property="og:description" content="Learn how to use the play command in CRAC Bot to play music from YouTube in your voice channel.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/play">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-purple-100 text-purple-800 px-2 py-1 rounded">Music</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Play Command</h1>
            <p class="text-xl text-gray-600">Play music from YouTube in your voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?play youtube_url
                    </div>
                    <p class="mb-4">The play command allows you to play audio from a YouTube video in your current voice channel.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">youtube_url</code> - The full URL of a YouTube video</li>
                        </ul>
                    </div>
                </section>

                <!-- URL Requirements Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">URL Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Accepted URL Formats:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Standard YouTube URLs (youtube.com/watch?v=...)</li>
                                <li>Short YouTube URLs (youtu.be/...)</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-yellow-50 rounded">
                            <p class="font-bold text-yellow-800 mb-2">Not Supported:</p>
                            <ul class="list-disc list-inside text-yellow-700">
                                <li>YouTube playlists</li>
                                <li>Non-YouTube URLs</li>
                                <li>YouTube Shorts</li>
                                <li>Live streams</li>
                                <li>Age-restricted videos</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Play with standard URL:</p>
                            <pre class="bg-gray-50 rounded p-4">?play https://www.youtube.com/watch?v=dQw4w9WgXcQ</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Play with short URL:</p>
                            <pre class="bg-gray-50 rounded p-4">?play https://youtu.be/dQw4w9WgXcQ</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Now Playing</p>
                                    <p class="text-gray-600">Title: Never Gonna Give You Up</p>
                                    <p class="text-gray-600">Channel: Rick Astley</p>
                                    <p class="text-gray-600">Duration: 3:32</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Invalid YouTube URL or video unavailable.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Speak
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Current Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>No queue system</li>
                        <li>Cannot pause/resume</li>
                        <li>No volume control</li>
                        <li>No skip function</li>
                        <li>One song at a time</li>
                        <li>Must wait for current song to finish</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Requirements</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Must be in a voice channel</li>
                        <li>Bot must have permission to join</li>
                        <li>Video must be public</li>
                        <li>Video must be available in your region</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\profile\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Profile Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Profile Command">
    <meta property="og:description" content="View detailed Discord profile information using CRAC Bot's profile command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/profile">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Profile Command</h1>
            <p class="text-xl text-gray-600">View detailed information about a user's Discord profile</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?profile @user
                    </div>
                    <p class="mb-4">The profile command displays comprehensive information about a user's Discord profile, including their roles, status, badges, and more.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to look up (mention required)</li>
                        </ul>
                    </div>
                </section>

                <!-- Profile Information Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Displayed Information</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Display Name</li>
                                <li>Username</li>
                                <li>User ID</li>
                                <li>Account Creation Date</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Status & Roles:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Current Status (Online/Offline/DND/Idle)</li>
                                <li>Top Role</li>
                                <li>All Roles List</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Visual Elements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Profile Picture</li>
                                <li>Banner (if available)</li>
                                <li>Discord Badges</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Look up user profile:</p>
                            <pre class="bg-gray-50 rounded p-4">?profile @UserName</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">UserName's Profile</p>
                                    <p class="text-gray-600">Display Name: UserName</p>
                                    <p class="text-gray-600">Username: User#1234</p>
                                    <p class="text-gray-600">User ID: 123456789012345678</p>
                                    <p class="text-gray-600">Creation Time: 17/10/24 12:34:56</p>
                                    <p class="text-gray-600">Status: 🟢 Online</p>
                                    <p class="text-gray-600">Top Role: @Admin</p>
                                    <p class="text-gray-600">Roles: @Admin, @Moderator, @Member</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Invalid Usage</p>
                                    <p class="text-red-600">Usage: ?profile @user</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>User not mentioned</li>
                        <li>User not in server</li>
                        <li>Invalid user mention</li>
                        <li>User account deleted</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Status Indicators</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>🟢 Online</li>
                        <li>⛔ Do Not Disturb</li>
                        <li>🟡 Idle</li>
                        <li>⚫ Offline</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Shows all available badges</li>
                        <li>Banner shown if available</li>
                        <li>Shows creation timestamp</li>
                        <li>Lists all user roles</li>
                        <li>Default avatar used if none set</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\quote\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Quote Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Quote Command">
    <meta property="og:description" content="Get a random famous quote using CRAC Bot's quote command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/quote">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Quote Command</h1>
            <p class="text-xl text-gray-600">Get an inspiring quote from a famous person</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?quote
                    </div>
                    <p class="mb-4">The quote command returns a random famous quote. Each use of the command provides a different quote from history's most notable figures.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Simply type ?quote</li>
                        </ul>
                    </div>
                </section>

                <!-- Example Quotes Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example Quotes</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-medium mb-2">Sample Responses:</p>
                            <ul class="space-y-4 text-gray-600">
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "Be the change you wish to see in the world."
                                    <div class="text-right font-bold mt-2">- Mahatma Gandhi</div>
                                </li>
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "I have not failed. I've just found 10,000 ways that won't work."
                                    <div class="text-right font-bold mt-2">- Thomas A. Edison</div>
                                </li>
                                <li class="p-4 bg-white rounded shadow-sm italic">
                                    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
                                    <div class="text-right font-bold mt-2">- Albert Einstein</div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Get a random quote:</p>
                            <pre class="bg-gray-50 rounded p-4">?quote</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Quote of the Moment ✨</p>
                                    <p class="text-gray-600 italic mt-2">"Success is not final, failure is not fatal: it is the courage to continue that counts."</p>
                                    <p class="text-gray-600 font-bold text-right mt-2">- Winston Churchill</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Quote Categories</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Inspirational</li>
                        <li>Historical</li>
                        <li>Scientific</li>
                        <li>Literary</li>
                        <li>Philosophical</li>
                        <li>Leadership</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Best Used For</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Daily inspiration</li>
                        <li>Starting discussions</li>
                        <li>Channel messages</li>
                        <li>Server greetings</li>
                        <li>Educational content</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Quotes from verified sources</li>
                        <li>Attribution included</li>
                        <li>Family-friendly content</li>
                        <li>Works in any channel</li>
                        <li>Random selection each time</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\server\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Server Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Server Command">
    <meta property="og:description" content="View detailed server statistics using CRAC Bot's server command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/server">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Server Command</h1>
            <p class="text-xl text-gray-600">View detailed statistics about the current Discord server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?server
                    </div>
                    <p class="mb-4">The server command displays comprehensive statistics and information about the current Discord server, including member counts, boost status, and more.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li>None required - Shows information for current server</li>
                        </ul>
                    </div>
                </section>

                <!-- Server Information Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Displayed Information</h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Basic Info:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Server Name</li>
                                <li>Server ID</li>
                                <li>Owner</li>
                                <li>Creation Date</li>
                                <li>Description (if set)</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Member Stats:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Total Members</li>
                                <li>Bot Count</li>
                                <li>Total Channels</li>
                                <li>Role Count</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Boost Information:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Boost Level</li>
                                <li>Total Boosts</li>
                            </ul>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Visual Elements:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Server Icon</li>
                                <li>Server Banner (if set)</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Example</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">View server stats:</p>
                            <pre class="bg-gray-50 rounded p-4">?server</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Server Name Server Stats</p>
                                    <p class="text-gray-600">Server ID: 123456789012345678</p>
                                    <p class="text-gray-600">Owner: @ServerOwner</p>
                                    <p class="text-gray-600">Created At: October 17, 2024 12:34:56 PM UTC</p>
                                    <p class="text-gray-600">Boost Level: Level 2</p>
                                    <p class="text-gray-600">Boost Count: 7</p>
                                    <p class="text-gray-600">Members: 1500</p>
                                    <p class="text-gray-600">Bots: 5</p>
                                    <p class="text-gray-600">Total Channels: 20</p>
                                    <p class="text-gray-600">Roles: 15</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Failed to fetch all members</li>
                        <li>HTTP connection errors</li>
                        <li>Permission errors</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Shows server banner if available</li>
                        <li>Displays server icon if set</li>
                        <li>Includes timestamp of check</li>
                        <li>Shows server description if set</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\timeout\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Timeout Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Timeout Command">
    <meta property="og:description" content="Learn how to use the timeout command in CRAC Bot to temporarily restrict users.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/timeout">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Timeout Command</h1>
            <p class="text-xl text-gray-600">Temporarily restrict a user's ability to interact with the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?timeout @user [duration] [unit] [reason]
                    </div>
                    <p class="mb-4">The timeout command temporarily prevents a user from sending messages, reacting to messages, or joining voice channels.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">@user</code> - The user to timeout (mention required)</li>
                            <li><code class="bg-gray-100 px-1 rounded">duration</code> - Number value for the timeout duration</li>
                            <li><code class="bg-gray-100 px-1 rounded">unit</code> - Time unit (s = seconds, m = minutes, h = hours, d = days)</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the timeout</li>
                        </ul>
                    </div>
                </section>

                <!-- Time Units Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Time Units</h2>
                    <div class="grid grid-cols-2 gap-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">s (Seconds)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 30 s</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">m (Minutes)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 5 m</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">h (Hours)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 2 h</code></p>
                        </div>
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold">d (Days)</p>
                            <p class="text-gray-600">Example: <code>?timeout @user 1 d</code></p>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic timeout (1 hour):</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 1 h</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Timeout with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 1 d Spamming in general chat</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Short timeout (5 minutes):</p>
                            <pre class="bg-gray-50 rounded p-4">?timeout @UserName 5 m Cool down period</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Timed Out</p>
                                    <p class="text-gray-600">@UserName has been timed out for 1 day.</p>
                                    <p class="text-gray-600">Reason: Spamming in general chat</p>
                                    <p class="text-gray-600">Timeout will expire: [timestamp]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Timeout Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/unban" class="text-blue-600 hover:text-blue-800">?unban</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Maximum timeout duration is 28 days</li>
                        <li>Bot must have a role higher than the user</li>
                        <li>Server owner cannot be timed out</li>
                        <li>The bot will attempt to DM the user</li>
                        <li>Timeouts are logged in the audit log</li>
                        <li>Users keep their roles during timeout</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Cannot combine time units</li>
                        <li>Time must be a whole number</li>
                        <li>Timed out users can still read messages</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\translate\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Translate Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Translate Command">
    <meta property="og:description" content="Learn how to translate text to English using CRAC Bot's translate command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/translate">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-green-100 text-green-800 px-2 py-1 rounded">Utility</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Translate Command</h1>
            <p class="text-xl text-gray-600">Translate text from any language to English</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?translate [text]
                    </div>
                    <p class="mb-4">The translate command automatically detects the language of the input text and translates it to English.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">text</code> - The text you want to translate to English</li>
                        </ul>
                    </div>
                </section>

                <!-- Language Support Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Language Support</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-gray-50 rounded">
                            <p class="font-bold mb-2">Features:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>Automatic language detection</li>
                                <li>Translation to English only</li>
                                <li>Support for most world languages</li>
                                <li>Handles special characters</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Spanish to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Hola, ¿cómo estás?</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">French to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Bonjour, comment allez-vous?</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">German to English:</p>
                            <pre class="bg-gray-50 rounded p-4">?translate Guten Tag, wie geht es dir?</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Translation</p>
                                    <p class="text-gray-600">Original (Spanish): Hola, ¿cómo estás?</p>
                                    <p class="text-gray-600">English: Hello, how are you?</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">Please provide text to translate. Usage: ?translate [text]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            None required
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>No text provided</li>
                        <li>Text too long</li>
                        <li>Unsupported characters</li>
                        <li>Connection errors</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Limitations</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>English output only</li>
                        <li>Text-only translation</li>
                        <li>No image translation</li>
                        <li>No custom language selection</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Tips</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Keep text concise for best results</li>
                        <li>Proper punctuation helps accuracy</li>
                        <li>Use complete sentences when possible</li>
                        <li>Original text is shown for reference</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\tts\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Text-to-Speech Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Text-to-Speech Command">
    <meta property="og:description" content="Convert text to speech using CRAC Bot's TTS command.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/tts">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-yellow-100 text-yellow-800 px-2 py-1 rounded">Fun</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Text-to-Speech Command</h1>
            <p class="text-xl text-gray-600">Convert text to speech and play it in a voice channel</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?tts [message]
                    </div>
                    <p class="mb-4">The TTS command converts your text message into speech and plays it in your current voice channel.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">message</code> - The text you want to convert to speech</li>
                        </ul>
                    </div>
                </section>

                <!-- Requirements Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Requirements</h2>
                    <div class="space-y-4">
                        <div class="p-4 bg-blue-50 rounded">
                            <p class="font-bold mb-2">Before Using:</p>
                            <ul class="list-disc list-inside text-gray-600">
                                <li>You must be in a voice channel</li>
                                <li>Bot needs permission to join voice channels</li>
                                <li>Bot needs permission to speak</li>
                                <li>Text must not be empty</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic message:</p>
                            <pre class="bg-gray-50 rounded p-4">?tts Hello everyone!</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Longer message:</p>
                            <pre class="bg-gray-50 rounded p-4">?tts Welcome to our Discord server. Hope you enjoy your stay!</pre>
                        </div>
                    </div>
                </section>

                <!-- Behavior Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Command Behavior</h2>
                    <div class="space-y-4">
                        <ol class="list-decimal list-inside space-y-2">
                            <li>Bot joins your voice channel</li>
                            <li>Converts text to speech</li>
                            <li>Plays the audio</li>
                            <li>Automatically disconnects after playing</li>
                            <li>Cleans up temporary audio files</li>
                        </ol>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">Ended TTS</p>
                                    <p class="text-gray-600">Successfully generated and played TTS file. Disconnecting from #General</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Join voice channel</p>
                                    <p class="text-red-600">Please join a voice channel to use this command! Usage: ?tts [message]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Connect
                        </li>
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Speak
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/join" class="text-blue-600 hover:text-blue-800">?join</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/leave" class="text-blue-600 hover:text-blue-800">?leave</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Common Issues</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Not in a voice channel</li>
                        <li>Missing message text</li>
                        <li>Bot lacks permissions</li>
                        <li>Channel at capacity</li>
                        <li>TTS generation fails</li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Good to Know</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>Auto-disconnects after playing</li>
                        <li>Stops current audio if playing</li>
                        <li>Works in any voice channel</li>
                        <li>Temporary files are cleaned up</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# commands\unban\index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Unban Command</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <meta property="og:title" content="CRAC Bot | Unban Command">
    <meta property="og:description" content="Learn how to use the unban command in CRAC Bot to remove bans from users.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/commands/unban">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
        pre {
            white-space: pre-wrap;
            word-wrap: break-word;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-12 p-6">
        <!-- Command Header -->
        <div class="mb-8">
            <div class="flex items-center gap-4 mb-4">
                <a href="https://crac.nerd-bear.org/commands" class="text-blue-600 hover:text-blue-800">← Back to Commands</a>
                <span class="text-xs bg-red-100 text-red-800 px-2 py-1 rounded">Moderation</span>
            </div>
            <h1 class="text-4xl font-bold mb-2">Unban Command</h1>
            <p class="text-xl text-gray-600">Remove a user's ban and allow them to rejoin the server</p>
        </div>

        <!-- Command Card Grid -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Main Content -->
            <div class="md:col-span-2 space-y-8">
                <!-- Usage Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Usage</h2>
                    <div class="bg-gray-50 rounded p-4 mb-4 font-mono">
                        ?unban user_id [reason]
                    </div>
                    <p class="mb-4">The unban command allows moderators to remove a ban from a user, allowing them to rejoin the server with a new invite.</p>
                    <div class="space-y-2">
                        <p><strong>Arguments:</strong></p>
                        <ul class="list-disc list-inside pl-4">
                            <li><code class="bg-gray-100 px-1 rounded">user_id</code> - The ID of the user to unban</li>
                            <li><code class="bg-gray-100 px-1 rounded">reason</code> - Optional: Reason for the unban</li>
                        </ul>
                    </div>
                </section>

                <!-- Finding User ID Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Finding a User's ID</h2>
                    <p class="mb-4">To unban a user, you'll need their User ID. Here's how to find it:</p>
                    <ol class="list-decimal list-inside space-y-2 mb-4">
                        <li>Enable Developer Mode in Discord (User Settings > App Settings > Advanced > Developer Mode)</li>
                        <li>Check the server's ban list (Server Settings > Bans)</li>
                        <li>Right-click on the user and select "Copy ID"</li>
                    </ol>
                    <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4">
                        <p class="text-yellow-700">
                            <strong>Note:</strong> User IDs are long numbers, like "123456789012345678"
                        </p>
                    </div>
                </section>

                <!-- Examples Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Examples</h2>
                    <div class="space-y-4">
                        <div>
                            <p class="font-medium mb-2">Basic unban:</p>
                            <pre class="bg-gray-50 rounded p-4">?unban 123456789012345678</pre>
                        </div>
                        <div>
                            <p class="font-medium mb-2">Unban with reason:</p>
                            <pre class="bg-gray-50 rounded p-4">?unban 123456789012345678 Appeal approved</pre>
                        </div>
                    </div>
                </section>

                <!-- Response Section -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h2 class="text-2xl font-bold mb-4">Bot Response</h2>
                    <div class="space-y-4">
                        <div class="border rounded p-4">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-gray-50 rounded p-4">
                                    <p class="font-medium">User Unbanned</p>
                                    <p class="text-gray-600">Successfully unbanned User#1234 (123456789012345678)</p>
                                    <p class="text-gray-600">Reason: Appeal approved</p>
                                </div>
                            </div>
                        </div>
                        <div class="border rounded p-4 border-red-200">
                            <div class="flex items-center gap-2 mb-2">
                                <div class="w-8 h-8 bg-blue-100 rounded-full"></div>
                                <span class="font-medium">CRAC Bot</span>
                            </div>
                            <div class="pl-10">
                                <div class="bg-red-50 rounded p-4">
                                    <p class="font-medium text-red-800">Error</p>
                                    <p class="text-red-600">User is not banned or ID is invalid.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            </div>

            <!-- Sidebar -->
            <div class="space-y-6">
                <!-- Required Permissions -->
                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Required Permissions</h3>
                    <ul class="space-y-2 text-gray-600">
                        <li class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            Ban Members
                        </li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Cooldown</h3>
                    <p class="text-gray-600">No cooldown</p>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Related Commands</h3>
                    <ul class="space-y-2">
                        <li><a href="https://crac.nerd-bear.org/commands/ban" class="text-blue-600 hover:text-blue-800">?ban</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/kick" class="text-blue-600 hover:text-blue-800">?kick</a></li>
                        <li><a href="https://crac.nerd-bear.org/commands/timeout" class="text-blue-600 hover:text-blue-800">?timeout</a></li>
                    </ul>
                </section>

                <section class="bg-white rounded-lg shadow-sm p-6">
                    <h3 class="text-xl font-bold mb-4">Additional Notes</h3>
                    <ul class="space-y-2 text-gray-600 list-disc list-inside">
                        <li>You must use the user's ID, not their username</li>
                        <li>The action is logged in the server's audit log</li>
                        <li>Users must be re-invited after being unbanned</li>
                        <li>The command works even if the user has left the server</li>
                    </ul>
                </section>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('main > *', {
                duration: 0.5,
                opacity: 0,
                y: 20,
                stagger: 0.1,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```

# home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC - Discord Bot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Home">
    <meta property="og:description" content="A versatile Discord bot for server management and user interaction. Features include moderation tools, customizable status, character info lookup, and message logging. Actively developed with frequent updates. Created by Nerd Bear for enhancing Discord communities.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-5xl font-bold mb-4 text-gray-900"><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Welcome to CRAC Bot</a></h2>
            <p class="text-xl mb-12 text-gray-600">The ultimate do-it-all Discord bot for moderation and fun!</p>
            <button id="cta-button" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-full transition shadow-lg">
                Add to Discord
            </button>
        </div>
    </main>

    <section id="features" class="container mx-auto mt-24 p-6">
        <h3 class="text-3xl font-bold mb-12 text-center text-gray-800">Features</h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Moderation</h4>
                <p class="text-gray-600">Powerful tools to keep your server safe and clean.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Fun Commands</h4>
                <p class="text-gray-600">Engage your community with interactive and entertaining commands.</p>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h4 class="text-xl font-bold mb-4 text-blue-600">Customization</h4>
                <p class="text-gray-600">Tailor CRAC to fit your server's unique needs.</p>
            </div>
        </div>
    </section>

    <div class="bg-blue-100 py-3 px-6 mt-12">
        <div class="container mx-auto text-center">
            <p class="text-blue-800">
                Recent changes to our <a href="https://crac.nerd-bear.org/privacy-policy" class="font-semibold underline hover:text-blue-600 transition">Privacy Policy</a>. Please review.
            </p>
        </div>
    </div>

    <footer class="bg-gray-200 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const ctaButton = document.getElementById('cta-button');
            
            ctaButton.addEventListener('mouseenter', () => {
                gsap.to(ctaButton, {scale: 1.05, duration: 0.3});
            });

            ctaButton.addEventListener('mouseleave', () => {
                gsap.to(ctaButton, {scale: 1, duration: 0.3});
            });

            // Easter egg
            let clickCount = 0;
            ctaButton.addEventListener('click', (e) => {
                window.location.href = "https://discord.com/oauth2/authorize?client_id=1289921476614553672&permissions=8&integration_type=0&scope=bot";
            });
        })
    </script>
</body>
</html>
```

# privacy-policy.html

```html
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CRAC - Discord Bot | Privacy Policy</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

        <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

        <!-- Open Graph Meta Tags (for Discord and other platforms) -->
        <meta property="og:title" content="CRAC Bot | Privacy Policy">
        <meta property="og:description" content="Privacy Policy for CRAC Bot - Learn how we collect, use, and protect your data when you use our Discord bot.">
        <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
        <meta property="og:url" content="https://crac.nerd-bear.org/privacy">
        <meta property="og:type" content="website">

        <style>
            .pfp-hover {
                transition: transform 0.3s ease-in-out;
            }
            
            .pfp-hover:hover {
                transform: scale(1.1);
            }
        </style>
    </head>

    <body class="bg-gray-50 text-gray-800">
        <nav class="container mx-auto p-6">
            <div class="flex justify-between items-center">
                <h1 class="text-3xl font-bold text-blue-600">
                    <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
                </h1>
                <ul class="flex space-x-6">
                    <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                    <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                    <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                    <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
                </ul>
            </div>
        </nav>

        <main class="container mx-auto mt-24 p-6">
            <div class="flex flex-col items-center mb-12">
                <a href="https://crac.nerd-bear.org/" class="mb-8">
                    <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
                </a>
                <h2 class="text-4xl font-bold mb-4 text-gray-900">
                    <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Privacy Policy</a>
                </h2>
            </div>
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Information We Collect</h3>
                <We class="mb-6">When you use CRAC Bot, we may collect certain information such as your Discord user ID, server ID, message content when using bot commands, and other relevant data necessary for the bot's functionality. We also have a Database of all the commands that users ran, and the hashed user ID. This is needed when moderators of a guild want to check what commands a user ran.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">2. How We Use Your Information</h3>
                <p class="mb-6">We use the collected information to provide and improve CRAC Bot's services, including command execution, server management, and user interaction. We do not sell or share your personal information with third parties.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">3. Data Storage and Security</h3>
                <p class="mb-6">We take reasonable measures to protect your data from unauthorized access or disclosure. However, no method of transmission over the internet or electronic storage is 100% secure.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Your Rights</h3>
                <p class="mb-6">You have the right to access, correct, or delete your personal information. To exercise these rights, please contact us using the information provided in the "Contact Us" section.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Changes to This Privacy Policy</h3>
                <p class="mb-6">We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Compliance with Discord's Policies</h3>
                <p class="mb-6">CRAC Bot complies with Discord's Developer Terms of Service and Developer Policy. We do not collect or use any data beyond what is necessary for the bot's functionality and what is allowed by Discord's policies.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Children's Privacy</h3>
                <p class="mb-6">CRAC Bot is not intended for use by children under the age of 13. We do not knowingly collect personal information from children under 13. If you are a parent or guardian and you are aware that your child has provided us with personal information,
                    please contact us.</p>

                <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Contact Us</h3>
                <p>If you have any questions about this Privacy Policy, please contact us at crac@nerd-bear.org.</p>
            </div>
        </main>

        <footer class="bg-gray-100 mt-24 py-8">
            <div class="container mx-auto text-center text-gray-600">
                <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
                <div class="mt-4">
                    <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                    <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                    <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
                </div>
            </div>
        </footer>
    </body>
</html>
```

# support.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Support</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Support">
    <meta property="og:description" content="Get help with CRAC Bot through our support articles or by contacting our support team.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/support">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">Support Center</h2>
            <p class="text-xl text-gray-600 mb-8">Get help with CRAC Bot</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            <!-- Help Articles Section -->
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold text-blue-600 mb-6">Help Articles</h3>
                <p class="text-gray-600 mb-6">Browse our collection of help articles to find answers to common questions:</p>
                <ul class="space-y-4">
                    <li>
                        <a href="https://crac.nerd-bear.org/support/article/commands-guide" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            Commands Guide
                        </a>
                    </li>
                    <li>
                        <a href="https://crac.nerd-bear.org/support/article/config-guide" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            Configuration Guide
                        </a>
                    </li>
                    <li>
                        <a href="https://crac.nerd-bear.org/support/article/add-feedback" class="flex items-center text-blue-600 hover:text-blue-800">
                            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                            </svg>
                            How to Submit Feedback
                        </a>
                    </li>
                </ul>
                <a href="https://crac.nerd-bear.org/articles" class="inline-block mt-6 text-blue-600 hover:text-blue-800">
                    View all articles →
                </a>
            </div>

            <!-- Contact Support Section -->
            <div class="bg-white p-8 rounded-lg shadow-md">
                <h3 class="text-2xl font-bold text-blue-600 mb-6">Contact Support</h3>
                <p class="text-gray-600 mb-6">Can't find what you're looking for? Our support team is here to help!</p>
                
                <div class="space-y-4">
                    <div class="flex items-center">
                        <svg class="w-6 h-6 mr-3 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                        </svg>
                        <a href="mailto:support@nerd-bear.org" class="text-blue-600 hover:text-blue-800">support@nerd-bear.org</a>
                    </div>
                    
                    <p class="text-gray-600 mt-6">Response Time: Within 24 hours</p>
                </div>

                <div class="mt-8 p-4 bg-blue-50 rounded-md">
                    <p class="text-sm text-blue-800">
                        <strong>Tip:</strong> For faster support, please include your server ID and a detailed description of your issue in your email.
                    </p>
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            gsap.from('.grid > div', {
                duration: 0.8,
                opacity: 0,
                y: 50,
                stagger: 0.2,
                ease: 'power3.out'
            });
        });
    </script>
</body>
</html>
```

# terms-of-use.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC - Discord Bot | Terms of Use</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">

    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Terms of Use">
    <meta property="og:description" content="Terms of Use for CRAC Bot - A versatile Discord bot for server management and user interaction. Please read these terms carefully before using CRAC Bot.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/terms">
    <meta property="og:type" content="website">
    
    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Terms of Use</a>
            </h2>
        </div>

        <div class="bg-white p-8 rounded-lg shadow-md">
            <h3 class="text-2xl font-bold mb-4 text-blue-600">1. Acceptance of Terms</h3>
            <p class="mb-6">By using CRAC Bot, you agree to these Terms of Use. If you disagree with any part of these terms, please do not use our bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">2. Use of the Bot</h3>
            <p class="mb-6">CRAC Bot is provided for Discord server management and entertainment purposes. You agree to use it only for its intended purposes and in compliance with Discord's Terms of Service.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">3. User Responsibilities</h3>
            <p class="mb-6">You are responsible for all activities that occur under your Discord account while using CRAC Bot. Do not use the bot for any illegal or unauthorized purpose.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">4. Modifications to Bot or Terms</h3>
            <p class="mb-6">We reserve the right to modify or discontinue CRAC Bot at any time. We may also revise these Terms of Use at our discretion. Continued use of the bot after any changes constitutes acceptance of those changes.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">5. Limitation of Liability</h3>
            <p class="mb-6">CRAC Bot is provided "as is" without warranties of any kind. We are not liable for any damages or losses related to your use of the bot.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">6. Privacy</h3>
            <p class="mb-6">Our use and collection of your information is governed by our Privacy Policy. By using CRAC Bot, you consent to our data practices as described in that policy.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">7. Termination</h3>
            <p class="mb-6">We may terminate or suspend your access to CRAC Bot immediately, without prior notice, for conduct that we believe violates these Terms of Use or is harmful to other users of the bot, us, or third parties, or for any other reason.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">8. Governing Law</h3>
            <p class="mb-6">These Terms shall be governed by and construed in accordance with the laws of United States of America and the United Kingdom, without regard to its conflict of law provisions.</p>

            <h3 class="text-2xl font-bold mb-4 text-blue-600">9. Contact Us</h3>
            <p>If you have any questions about these Terms, please contact us at crac@nerd-bear.org.</p>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>
</body>
</html>
```

# versions.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRAC Bot - Version History</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.4/gsap.min.js"></script>

    <link rel="icon" type="image/png" href="http://nerd-bear.org/favicon.ico">
    
    <!-- Open Graph Meta Tags (for Discord and other platforms) -->
    <meta property="og:title" content="CRAC Bot | Version History">
    <meta property="og:description" content="Explore the version history of CRAC Bot, a versatile Discord bot for server management and user interaction. See the latest updates, features, and improvements.">
    <meta property="og:image" content="https://crac.nerd-bear.org/pfp-5.png">
    <meta property="og:url" content="https://crac.nerd-bear.org/versions">
    <meta property="og:type" content="website">

    <style>
        .pfp-hover {
            transition: transform 0.3s ease-in-out;
        }
        .pfp-hover:hover {
            transform: scale(1.1);
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
    <nav class="container mx-auto p-6">
        <div class="flex justify-between items-center">
            <h1 class="text-3xl font-bold text-blue-600">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-800 transition">CRAC Bot</a>
            </h1>
            <ul class="flex space-x-6">
                <li><a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">Home</a></li>
                <li><a href="https://crac.nerd-bear.org/commands" class="hover:text-blue-600 transition">Commands</a></li>
                <li><a href="https://crac.nerd-bear.org/versions" class="hover:text-blue-600 transition">Versions</a></li>
                <li><a href="https://crac.nerd-bear.org/support" class="hover:text-blue-600 transition">Support</a></li>
            </ul>
        </div>
    </nav>

    <main class="container mx-auto mt-24 p-6">
        <div class="flex flex-col items-center mb-12">
            <a href="https://crac.nerd-bear.org/" class="mb-8">
                <img src="https://crac.nerd-bear.org/pfp-5.png" alt="CRAC Bot" class="rounded-full shadow-lg w-32 h-32 object-cover pfp-hover">
            </a>
            <h2 class="text-4xl font-bold mb-4 text-gray-900">
                <a href="https://crac.nerd-bear.org/" class="hover:text-blue-600 transition">CRAC Bot Version History</a>
            </h2>
        </div>
        
        <div class="mb-8">
            <input type="text" id="search-input" placeholder="Search versions..." class="w-full p-2 border border-gray-300 rounded-md">
        </div>

        <div class="mb-8" id="toc">
            <h3 class="text-2xl font-bold mb-4">Table of Contents</h3>
            <ul class="space-y-2">
                <li><a href="#v0-4-4" class="text-blue-600 hover:underline">CRAC 0.4.4 Beta pre-release</a></li>
                <li><a href="#v0-4-3" class="text-blue-600 hover:underline">CRAC 0.4.3 Beta pre-release</a></li>
                <li><a href="#v0-4-2" class="text-blue-600 hover:underline">CRAC 0.4.2 Beta pre-release</a></li>
                <li><a href="#v0-4-1" class="text-blue-600 hover:underline">CRAC 0.4.1 Beta pre-release</a></li>
            </ul>
        </div>
        
        <div class="space-y-12" id="versions-container">
            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-4">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.4 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.04 MB (~43.1 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 05/10/2024 2:45 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.4" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.4</a>
                
                <p class="mb-4">This is a simple beta testing release with around 17 simple commands, the commands are: help, charinfo, tts, profile, play, join, leave, timeout, kick, ban, unban, shutdown, start, stream, play, watch, and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>Ban & Unban commands don't handle all exceptions and may cause undefined/buggy behaviour</li>
                    <li>There is no untimeout command and timeouts can only be in one unit of one amount</li>
                    <li>Status config commands still exist and have not been removed yet</li>
                    <li>Join/leave commands still not added to help embed</li>
                    <li>Many commands missing proper or any error handling</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Changed the default Logger construct-er log output path to ./logs/output.log instead of ./logs/output.log</li>
                    <li>Added tts command</li>
                    <li>Added tts command to the help embed</li>
                    <li>Added leave command</li>
                    <li>Added join command</li>
                    <li>Added run logs to join the command</li>
                    <li>Added run logs to leave command</li>
                    <li>Added run logs to TTS command</li>
                    <li>Changed tts command messages to be embedded</li>
                    <li>Added more error handling to the tts command</li>
                    <li>Updated tts command success embed to have a channel link and not a name</li>
                    <li>Added play command</li>
                    <li>Patched play command to not leave after starting to play</li>
                    <li>Added play command to help embed</li>
                    <li>Added profile command</li>
                    <li>Added profile command to help embed</li>
                    <li>Added failsafes and exception handling in the profile command</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-blue-600">Update notes:</h4>
                <p class="mb-4">I will remove all status config commands as they affect the bot across all guilds (Servers) and are just added as a proof of concept. The commands and features I will be adding are config files, untimeout commands, voice chat mute commands, per guild config, music features, and other fun features! Another feature, probably the biggest one (since it will allow for a lot of new features) will be the music queue backend change since it will allow for many new features.</p>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-3">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.3 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.03 MB (~30.8 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 04/10/2024 2:17 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.3" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.3</a>
                
                <p class="mb-4">This is a simple beta testing release with around 12 simple commands, the commands are: help, charinfo, timeout, kick, ban, unban, shutdown, start, stream, play, watch, and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behavior, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>Ban & Unban commands don't handle all exceptions and may cause undefined/buggy behavior</li>
                    <li>There is no untimeout command and timeouts can only be in one unit of one amount</li>
                    <li>Status config commands still exist and have not been removed yet</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Added unban command</li>
                    <li>Added unban command to help embed</li>
                    <li>Added exception handling to all cases of unban command</li>
                    <li>Changed Bot Intents from default to all</li>
                    <li>Changed the Logger class constructer to default to a relative output path</li>
                    <li>Ran blacklint on source code to increase readability</li>
                    <li>Specified bot command parameter types for syntax highlighting</li>
                    <li>Added timeout command</li>
                    <li>Added timeout command to help embed</li>
                    <li>Changed the timeout command to send a dm to the user</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-blue-600">Update notes:</h4>
                <p class="mb-4">I will be removing all status config commands as they affect the bot across all guilds (Servers) and are just added as a proof of concept. The commands and features I will be adding are config files, untimeout command, voice chat mute commands, per guild config, music features, and other fun features!</p>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-2">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.2 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 03/10/2024 3:39 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.2" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.2</a>
                
                <p class="mb-4">This is a simple beta testing release with around 10 simple commands, the commands are: help, charinfo, kick, ban, shutdown, start, stream, play, watch and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>The charinfo command still has no support for a large number of special characters</li>
                    <li>More unknown issues may exist</li>
                </ul>

                <h4 class="text-xl font-bold mb-2 text-green-600">Change log:</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>Removed all logger.info logs</li>
                    <li>Added footer to the DM_EMBED of the word filter</li>
                    <li>Added the charinfo command to the help embed</li>
                    <li>Changed the logger initialization to be a relative logger output path</li>
                    <li>Added logger info level logs to show what user ran what command when</li>
                </ul>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>

            <div class="bg-white p-8 rounded-lg shadow-md" id="v0-4-1">
                <h3 class="text-2xl font-bold text-blue-600 mb-4">CRAC 0.4.1 Beta pre-release 🧪</h3>
                <p class="mb-2"><strong>Program size:</strong> ~0.02 MB (~18.3 KB)</p>
                <p class="mb-4"><strong>Release date:</strong> 02/10/2024 4:09 AM BST</p>
                <a href="https://github.com/nerd-bear/CRAC/releases/tag/0.4.1" class="inline-block mb-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition">Download v0.4.1</a>
                
                <p class="mb-4">This is a simple beta testing release with around 10 simple commands, the commands are: help, charinfo, kick, ban, shutdown, start, stream, play, watch and listen. Nearly daily updates are to be expected.</p>
                
                <h4 class="text-xl font-bold mb-2 text-red-600">Warnings</h4>
                <ul class="list-disc list-inside mb-4 space-y-1">
                    <li>This version contains the usage of deprecated classes/functions and similar.</li>
                    <li>Unstable and not defined behaviour, this version might contain errors that are not handled properly or at all and general bugs.</li>
                    <li>No proper separation, this program version is currently a relative mess and not well structured, which may cause issues when customizing and or setting the bot up.</li>
                    <li>May include hard-coded paths to files that may not exist or path formats meant for another OS</li>
                    <li>More unknown issues may exist</li>
                </ul>
                
                <p class="text-sm text-gray-600 italic">Created by Nerd Bear (This version of CRAC is open source and under the apache2 license)</p>
            </div>
        </div>
    </main>

    <footer class="bg-gray-100 mt-24 py-8">
        <div class="container mx-auto text-center text-gray-600">
            <p>&copy; 2024 CRAC Bot. All rights reserved.</p>
            <div class="mt-4">
                <a href="https://crac.nerd-bear.org/privacy-policy" class="text-blue-600 hover:text-blue-800 mx-2">Privacy Policy</a>
                <a href="https://crac.nerd-bear.org/terms-of-use" class="text-blue-600 hover:text-blue-800 mx-2">Terms of Use</a>
                <a href="https://crac.nerd-bear.org/support" class="text-blue-600 hover:text-blue-800 mx-2">Support</a>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const searchInput = document.getElementById('search-input');
            const versionContainers = document.querySelectorAll('#versions-container > div');

            // Search functionality
            searchInput.addEventListener('input', () => {
                const searchTerm = searchInput.value.toLowerCase();

                versionContainers.forEach(container => {
                    const versionContent = container.textContent.toLowerCase();
                    if (versionContent.includes(searchTerm)) {
                        container.style.display = 'block';
                    } else {
                        container.style.display = 'none';
                    }
                });
            });

            // Animation
            gsap.from('#versions-container > div', {
                duration: 0.5,
                opacity: 0,
                y: 50,
                stagger: 0.2,
                ease: 'power2.out'
            });
        });
    </script>
</body>
</html>
```