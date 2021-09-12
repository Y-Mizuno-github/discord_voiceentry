import discord

client = discord.Client()

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        botRoom = client.get_channel(Channel)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [VoiceChannels]

        # 入室通知
        if after.channel is not None and after.channel.id in announceChannelIds and after.channel is not before.channel:
            await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加しました！")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run("TOKEN")
