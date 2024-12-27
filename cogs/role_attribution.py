from discord.ext import commands

ROLE_ID = "The role ID you wanna look up to, should be a serie of numbers"
MESSAGE_ID = "The message ID you wanna look up to, should be a serie of numbers"
EMOJI = "put an emoji there, still astonished we can put emojis in code now"

class RoleReaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
            guild = self.bot.get_guild(payload.guild_id)
            role = guild.get_role(ROLE_ID)
            member = guild.get_member(payload.user_id)
            if role and member:
                await member.add_roles(role)
                print(f"Role {role.name} attributed to {member.name}.")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == MESSAGE_ID and str(payload.emoji) == EMOJI:
            guild = self.bot.get_guild(payload.guild_id)
            role = guild.get_role(ROLE_ID)
            member = guild.get_member(payload.user_id)
            if role and member:
                await member.remove_roles(role)
                print(f"Role {role.name} removed from {member.name}.")

async def setup(bot):
    await bot.add_cog(RoleReaction(bot))
