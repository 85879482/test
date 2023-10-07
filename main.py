bot.send_message(
                    self.user.id,
                    "\n".join(
                        (
                            lang_full("verify_challenge"),
                            "",
                            code(lang_full("verify_send_sticker")),
                            "",
                            lang_full(
                                "verify_challenge_timed", timeout if timeout > 0 else ""
                            ),
                        )
                    )
