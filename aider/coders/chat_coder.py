#!/usr/bin/env python

from aider.coders.ask_coder import AskCoder
from aider.coders.base_prompts import CoderPrompts

class ChatPrompts(CoderPrompts):
    main_system = """You are a Senior Software Engineer with over 15 years of experience in software development, specializing in explaining complex technical concepts in a simple, intuitive, and beginner-friendly way. Your goal is to assist me by answering my questions, breaking down programming concepts, tools, or technologies into easy-to-understand terms, and teaching me as if I’m a curious learner (assume I have basic knowledge but may need guidance). Use analogies, real-world examples, or step-by-step explanations when possible to make things clear and engaging. If I ask about code, provide concise, practical examples (in a language I specify or suggest one if I don’t). Be patient, encouraging, and proactive—offer additional tips or context where relevant to help me learn faster. If I’m unclear or need clarification, gently ask follow-up questions to tailor your response. Avoid jargon unless you explain it, and keep the tone friendly, approachable, and mentor-like.
"""

    system_reminder = ""

    # Empty these prompts since we don't need repository/file context
    repo_content_prefix = ""
    files_content_prefix = ""
    files_no_full_files = ""
    files_no_full_files_with_repo_map = ""
    read_only_files_prefix = ""
    shell_cmd_prompt = ""
    no_shell_cmd_prompt = ""
    shell_cmd_reminder = ""
    no_shell_cmd_reminder = ""

class ChatCoder(AskCoder):
    """Simple chat without sending any repository context.
    
    This coder provides a clean conversation interface with no code context,
    making it useful for general discussions, brainstorming, or conversations
    unrelated to the current codebase.
    """

    edit_format = "chat"
    gpt_prompts = ChatPrompts()
    
    def get_repo_messages(self):
        """Override to return empty list - no repo context in chat mode"""
        return []
    
    def get_readonly_files_messages(self):
        """Override to return empty list - no readonly files in chat mode"""
        return []
    
    def get_chat_files_messages(self):
        """Override to return empty list - no files in chat mode"""
        return []
    
    def get_repo_map(self, force_refresh=False):
        """Override to ensure repo map is never included"""
        return None
    
    def fmt_system_prompt(self, prompt):
        """Override to provide a chat-specific system prompt"""
        # Keep standard prompt formatting but add clarity about chat mode
        formatted = super().fmt_system_prompt(prompt)
        chat_mode_notice = "\nYou are in chat mode. No repository context is provided."
        return formatted + chat_mode_notice
