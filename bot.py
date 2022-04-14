import discord
import asyncio

client = discord.Client()

token = "ODgwMzU1NTA2MzQ1MTE1NjQ5.YSdE9A.UBCSARI8XPrdhkjB9JT3m04O754"


@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("League of Legends")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)
  
@client.event

async def on_message(message):

    if message.content.startswith('!사미라 패시브'):   
          embed = discord.Embed(title="패시브", description="무모한 충동", color=0xAAFFFF) 
          embed.add_field(name="무모한 충동 - 효과1", value="기본 공격 또는 스킬로 적 챔피언에게 피해를 입히면 콤보를 1회 쌓습니다. E부터 S까지 총 6등급을 쌓을수 있습니다. 근접 공격 사거리 내에 있는 적에게 스킬을 사용하거나 기본 공격을 가하면 추가 마법 피해를 입힙니다. 피해량은 대상이 잃은 체력에 비례하여 2배까지 증가합니다. ", inline=False) 
          embed.add_field(name="무모한 충동 - 효과2", value="사미라가 근접 공격 사거리 내에 있는 적에게 스킬을 사용하거나 기본 공격을 가하면 추가 마법 피해를 입힙니다. 피해량은 대상이 잃은 체력에 비례하여 2배까지 증가합니다. ", inline=False)
          embed.add_field(name="무모한 충동 - 효과3", value="사미라가 이동 불가 효과에 영향을 받은 적에게 기본 공격을 가하면 최대 사거리까지 돌진합니다. 해당 적이 공중으로 띄워진 상태라면 사미라도 최소 0.5초간 롤아이콘-군중제어 에어본공중으로 띄워 올립니다.", inline=False)
          embed.set_footer(text="평타, 스킬을 통틀어 이전에 입힌 것과 다른 공격을 적중시키면 콤보가 중첩 시킬 수 있으며, 콤보에 따라 최대 6회 까지 쌓을 수 있습니다. 지속시간은 6초 입니다.")      
          embed.set_thumbnail(url="https://ww.namu.la/s/7925145139c1c3a65fbfa666f4476880944020cfa554e6d7cdd3df2c8d227ad8275ebd499d6350236692a6c7477954a2fb68b0104bd5ad1c652cb67c63593bbdc69d3dd73dc69eeb5db2fcd23ede8daacf773c9aebd08187cee64aa8726e4825") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!사미라 Q'): 
          embed = discord.Embed(title="천부적 재능", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 천부적 재능", value="사미라가 총을 쏴 처음 맞은 적에게 물리 피해를 입힙니다. 근접 공격 사거리 내에 있는 적에게 이 스킬을 사용하면, 사미라가 검으로 베어 물리 피해를 입힙니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="두 공격 모두 치명타가 적용되어 25%의 추가 피해를 입힐 수 있으며 66.6%의 생명력 흡수 효과가 적용됩니다. 거침없는 질주 도중 사용하면 돌진이 끝난 후 경로 내에 있는 모든 적을 공격합니다.", inline=False)
          embed.set_footer(text="6초 / 5초 / 4초 / 3초 / 2초")
          embed.set_thumbnail(url="https://ww.namu.la/s/0153aa65b65f3dde2004bb6750c6e10f5b3cff20fd22f165e5978667327b6f68176c111d46fa207ec7c2a525d8c1cca53d22966a2bead73128f53d43e6c523980405d960f4f9e1fe5f851c043462b1e90ff0757c3eff934b9d714eccaf1693a7") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!사미라 W'): 
          embed = discord.Embed(title="원형검무", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 원형 검무", value="사미라가 0.75초 동안 주변에 검을 휘두르며 적들을 두 번 공격해 각각 물리 피해를 입히고 범위 안으로 들어오는 적의 투사체를 모두 파괴합니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="W 지속 시간 도중 E와 R을 사용할 수 있습니다.", inline=False) 
          embed.set_footer(text="30초 / 28초 / 26초 / 24초 / 22초")
          embed.set_thumbnail(url="https://w.namu.la/s/e4d3fbc95de16aef77884bdbaadbf9be3b15ab21080638d7eb9b1bd50199628fa9b010a05a51c7f688901a0bf416ccb6b24d35d83262cb67f7ee202731713984b666728c0ddb515129b1452ad1aad842d776f17711c2eff20c16a2cfee4ea7cb") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!사미라 E'): 
          embed = discord.Embed(title="거침없는 질주", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 거침없는 질주", value="사미라가 적(포탑 포함)을 통과해 돌진합니다. 돌진 도중 통과하는 모든 적을 베어 마법 피해를 입히고, 3초 동안 공격 속도를 얻습니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="사미라가 피해를 입힌 적 챔피언이 3초 안에 처치되면 거침없는 질주의 재사용 대기시간이 초기화됩니다.", inline=False) 
          embed.set_footer(text="20초 / 18초 / 16초 / 14초 / 12초")
          embed.set_thumbnail(url="https://ww.namu.la/s/d747a09d4d93b4d5fbbc155b3f482ce8f9a572795acefc9709e4a5263c48b8652ccbfd967d3ad0fd20e03fa0bd5c8dc838eca90040f896a0836090e6c63bd880fbe5b0c88518b7f952c2a5687a045f8a5c33c482100aeb094d7a1c13db9dd77b") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!사미라 R'): 
          embed = discord.Embed(title="지옥불 난사", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 지옥불 난사", value="사미라의 스타일 등급이 S등급일 때만 이 스킬을 사용할 수 있습니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="사미라가 무기를 난사해 2초 동안 10회에 걸쳐 주변의 모든 적에게 공격을 퍼붓습니다. 각 사격은 물리 피해를 입히며 66.6%의 생명력 흡수가 적용됩니다. 또한 치명타가 적용될 수 있습니다. 미니언에겐 25%의 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="8초")
          embed.set_thumbnail(url="https://w.namu.la/s/123bad3d8a92663025d00ffeb696984aaf57632a5f26f69b29597c5c1684a566bf5e92112f3649ce64fff10701f45edad8b1e3a541089509fd4eecfe4e27812a4f146c7c4e2a0a761599d6df20625dacf9330cfcedb1c6ebae3a2855c49beeaa") 
          await message.channel.send(embed=embed)
 
    elif message.content.startswith('!진 패시브'):
          embed = discord.Embed(title="속삭임", description=" ", color=0xAAFFFF) 
          embed.add_field(name="속삭임", value="진이 사용하는 총은 공격 속도가 고정되어 있으며 4발을 발사한 후엔 재장전해야 합니다. 4번째 총탄은 언제나 치명타가 발동되며, 대상이 잃은 체력만큼 추가 물리 피해를 입힙니다. 추가 효과: 진이 추가 공격력을 얻습니다. 진의 치명타 피해량이 14% 감소하지만, 2초 동안 이동 속도가 10% (+0.4 추가 공격 속도) 증가합니다.", inline=False) 
          embed.set_footer(text="공격력은 치명타 확률과 추가 공격 속도에 비례합니다. 이동 속도는 추가 공격 속도에 비례합니다.")      
          embed.set_thumbnail(url="https://w.namu.la/s/4d69c05919bc9fbd4e4e27a07d4a430b43170eb95fe5ba5f1924acad86b3b330beb6dcf3fe87ed6cbdf19a05aee558471463a8732b3adfdd44ee6ce9d5fa146243fa6f9dfa5ec98effc295ba4cc56aa5e14f2f87c7fa92d9253ea72e404e2cb7") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!진 Q'): 
          embed = discord.Embed(title="춤추는 유탄", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 춤추는 유탄", value="진이 폭탄을 던져 물리 피해를 입힌 후 아직 폭탄에 맞지 않은 근처의 적에게 튕깁니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="폭탄은 최대 4번까지 적을 맞힐 수 있으며, 폭탄으로 적을 처치할 때마다 그 다음 타격의 피해량이 35%씩 늘어납니다.", inline=False) 
          embed.set_footer(text=" 7초 / 6.5초 / 6초 / 5.5초 / 5초")
          embed.set_thumbnail(url="https://ww.namu.la/s/290c2bf76e3a34bce6f6fa148582c581eddd2a620910c11ccf61d294329f81455e350086140d892c6568790414b249d2739d8176f5524b1cc5bb50d1de6cfa3b093ffb7fc1896c694e3cdde86dafcea197c1786a90c7cb96f52a272a71ef37d9") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!진 W'): 
          embed = discord.Embed(title="살상연희", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 살상연희", value="진이 원거리 공격을 가하여 처음 적중한 챔피언에게 물리 피해를 입히고 경로상에 있는 다른 모든 적에게 75%의 피해를 입힙니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="이 스킬로 아군 챔피언 에게 공격당한 챔피언을 4초 안에 공격했다면 대상을 일정 시간 동안 속박하고 속삭임의 이동 속도가 증가합니다. 강제 관람으로 설치한 함정을 밟은 적들도 속박됩니다.", inline=False) 
          embed.set_footer(text="12초")
          embed.set_thumbnail(url="https://w.namu.la/s/ed0144b787b7b18d0a29f27a17e1174bc38203293a3177d99ee04129b30045aebe8cf740e66faad5c5fe44f00012fefac4db8a928edc2ac86ef5122a021af31f9a0b81e83c9ef2ef822a5cf313edd103d80035fab5a69d659876a86ca6cc7208") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!진 E'): 
          embed = discord.Embed(title="강제 관람", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 강제 관람", value="기본 지속 효과: 진이 적 챔피언을 처치하면 해당 위치에 연꽃 함정이 설치되어 폭발합니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="사용 시: 진이 3분 동안 유지되는 보이지 않는 연꽃 함정을 설치합니다. 함정을 밟은 적은 35% 둔화됩니다. 함정은 2초 후 폭발하여 마법 피해를 입힙니다. 이 스킬은 2회까지 충전됩니다. 연꽃 함정은 챔피언이 아닌 대상과 최근에 다른 연꽃 함정에 적중한 챔피언에게 65%의 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="28초 / 25초 / 22초 / 19초 / 16초마다 충전됩니다.")
          embed.set_thumbnail(url="https://w.namu.la/s/05d96982d3998082b198e1f14e7d6d2f5587600a99b95cedd3129e028ab408354e42b50864e6c9dc5d188368757c7e8e9eb2a232a20b37b39ebafa161311752f889925c05d405fef7714d234d954cdc49ee3f676613695ab30b7e9dc37e6c670d28b69d370c5bc543d10922429ed0ba3") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!진 R'):
          embed = discord.Embed(title="커튼 콜", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 커튼 콜", value="진이 자세를 잡고 정신을 집중해 4발의 강력한 탄환을 발사합니다.", inline=False)           
          embed.add_field(name="스킬 효과 - 1", value="각 탄환은 처음 적중한 챔피언에게 대상이 잃은 체력에 비례해 물리 피해를 입히고 0.5초 동안 80% 둔화시킵니다.", inline=False) 
          embed.add_field(name="스킬 효과 - 2", value="4번째 총탄은 치명타가 발동되며 200%만큼 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="120초 / 105초 / 90초")
          embed.set_thumbnail(url="https://w.namu.la/s/9aae5812ddf38887e0b77ee346dc9527b2362730f75370f6def19c7ed9c7aeb3d84cd42b9462f2feb17a6c7e9dc866a3425c447431e7c981e63656d310ca40422004cfaa4f6dd8b10ea480428da4c659c5e3e24287c0085bbd84c54279b08da5")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!미스포츈 패시브'):
          embed = discord.Embed(title="사랑의 한 방", description=" ", color=0xAAFFFF) 
          embed.add_field(name="사랑의 한 방", value="미스 포츈이 새로운 대상에게 기본 공격을 가하면 물리 피해를 추가로 입힙니다.", inline=False) 
          embed.set_footer(text="모든 공격에 패시브가 전부 다 적용됩니다.")      
          embed.set_thumbnail(url="https://ww.namu.la/s/22b43bddfb66ab30d27a979016a74c487abc488f46d864de7e0ea4ebacdd5d745de9adbe302bd6e1e2b6ee07f4e84aa1aca5055233477d84b951355f28d71c3372ec11bb0fb148ea2cc1acb2e97fc47d98c86960b83f3b6931d46a2c063b739c") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!미스포츈 Q'): 
          embed = discord.Embed(title="한 발에 두 놈", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 한 발에 두 놈", value="미스 포츈이 튕기는 총알을 발사하여 적 하나와 그 뒤에 있는 다른 적에게 각각 물리 피해를 입힙니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="두 번째 대상에게는 치명타를 입힐 수 있으며, 첫 번째 대상을 처치했을 경우 두 번째 대상에게는 항상 치명타가 적용됩니다.", inline=False) 
          embed.set_footer(text=" 7초 / 6초 / 5초 / 4초 / 3초")
          embed.set_thumbnail(url="https://ww.namu.la/s/9cfebc9b16ff2ca61e865234b3d98bd9277df749f65b80a2a0c14e0e3706a0e9aca1bcd2d02c3c05c501c6214b5d0c87a1310499e780b72c5a649584a3418845853353ffd0c7559953f6e7b3b95f7591a63b4f643f8cb3452feae63dcd50120a") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!미스포츈 W'): 
          embed = discord.Embed(title="활보", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 활보", value="기본 지속 효과: 5초간 피해를 받지 않으면 미스 포츈의 이동 속도가 25 증가합니다. 다음 5초간 피해를 입지 않으면 이동 속도가 최대치까지 증가합니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="사용 시: 이동 속도 증가 효과를 최대로 얻고 4초 동안 공격 속도가 상승합니다.", inline=False) 
          embed.add_field(name="상세 효과", value="이동속도 - 55 / 65 / 75 / 85 / 95 \n 공격속도 -  40 / 55 / 70 / 85 / 100% ", inline=False) 
          embed.set_footer(text="12초")
          embed.set_thumbnail(url="https://w.namu.la/s/066e09f224b119b44313af4b08abac69268b58a2bc5445fceed87df4b8c7d205b36f78cee11669c81799e912631263ecdd2d638aea74b4eb2b1547e4549d5b96a9958d0e033ba1b782eda069a723e0b4d3ca800ac35d78ee199508ffc2036b8a") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!미스포츈 E'): 
          embed = discord.Embed(title="총알은 비를 타고", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 총알은 비를 타고", value="미스 포츈이 지정 지역에 총알을 퍼부어 시야를 밝히고 2초간 마법 피해를 입힙니다. 총알에 맞은 적은 둔화됩니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="해당 지역에 총알을 퍼부어 0.25초마다 마법 피해를 입히고 둔화시켜 2초 동안 총 8번을 타격한다.", inline=False) 
          embed.set_footer(text="18초 / 16초 / 14초 / 12초 / 10초")
          embed.set_thumbnail(url="https://ww.namu.la/s/58e98f78dda8bbfaa690ae36084e279e18cbb0467d03bb8fc675667f91c2fc5381115523fc46b7f01690aef8f31f8f129ef9fe3117bd2c4ed0cb3494c19e7f77cdc49be0fd21ac62697f59c5fe6c6ad9c10c0f32865a2f896b5887e37ce4f334") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!미스포츈 R'):
          embed = discord.Embed(title="쌍권총 난사", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 쌍권총 난사", value="미스 포츈이 3초 동안 정신 집중 상태로 총을 난사해 공격 한 차례에 물리 피해를 입힙니다.", inline=False)           
          embed.add_field(name="스킬 효과", value="이 스킬은 매회 발사 시 각각 120%의 치명타 피해를 입힐 수 있습니다.", inline=False) 
          embed.set_footer(text="120초 / 110초 / 100초")
          embed.set_thumbnail(url="https://ww.namu.la/s/58db3f5e5329f1be184e4f755e302dc59a00acd7b1a82ec815ccd0f13fcd8cfa57c1f703f583dfb60a3de39579362ae2373b7d5c9a4651f839614339da943660342a8af74ac599facc645fff9162cb22d2e3e2a490a77aa889b11af87de8cfa2")
          await message.channel.send(embed=embed)
 
    elif message.content.startswith('!케이틀린 패시브'):
          embed = discord.Embed(title="헤드샷", description=" ", color=0xAAFFFF) 
          embed.add_field(name="헤드샷", value="6번째 기본 공격마다 케이틀린이 헤드샷을 발사합니다. 수풀 안에서 공격하면 헤드샷에 필요한 기본 공격을 2회 한 것으로 간주합니다.", inline=False) 
          embed.add_field(name="추가 효과", value="헤드샷은 물리 피해를 추가로 입힙니다. 요들잡이 덫에 적중한 적을 대상으로 할 때는 사거리가 두 배로 늘어나고 물리 피해 역시 추가됩니다. 90구경 투망에 적중한 적을 대상으로 할 때는 사거리만 두 배로 늘어납니다.", inline=False)  
          embed.set_thumbnail(url="https://w.namu.la/s/54ebd706961203eda58b79b393d78dde2d1c047f1e9c6b5a503757efa95964694c6c5433daafd3bf7ae6f3b0453ee8db44874f63358be3ebb2b5493db147da15e31473b6553f8b04207a5b2ff606b6dc3d65d9fba73dff80677a9ae6006c1d3f") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!케이틀린 Q'): 
          embed = discord.Embed(title="필트오버 피스메이커", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 필트오버 피스메이커", value="케이틀린이 조준한 후 적을 관통하는 총알을 발사하여 물리 피해를 입힙니다. 첫 번째 대상에게 적중한 후에는 탄도체 유효 범위가 넓어지며 60%의 물리 피해를 입힙니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="요들잡이 덫 때문에 위치가 드러난 적은 항상 100%의 피해를 입습니다.", inline=False) 
          embed.set_footer(text=" 10초 / 9초 / 8초 / 7초 / 6초")
          embed.set_thumbnail(url="https://ww.namu.la/s/e404230e8e832a5123f9f34dc445214ec8eab6d8d610b5d514d44b2619b89b7f27ab1b24f04b0cb7958633c5358e6af48f2534fb8b26999f6bd58b6c63c058a0f777e0b7a4a404546331d5ae291027c25a55f395d6f87bf81d68647408287a92") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!케이틀린 W'): 
          embed = discord.Embed(title="요들잡이 덫", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 요들잡이 덫", value="케이틀린이 덫을 설치하여 처음 밟는 적을 1.5초 동안 속박하고 3초 동안 절대 시야를 얻으며, 대상에게 케이틀린의 헤드샷이 강화됩니다. 덫은 일정 시간 동안 지속되며, 한 번에 일정 개수까지 설치할 수 있습니다. 이 스킬은 2회까지 충전됩니다.", inline=False)  
          embed.add_field(name="상세 효과", value="충전 시간:30초 / 25.5초 / 21초 / 16.5초 / 12초 \n 설치 가능 개수: 3 / 3 / 4 / 4 / 5 \n 지속 시간: 30 / 35 / 40 / 45 / 50", inline=False) 
          embed.set_footer(text="헤드샷 피해량 증가: 60 / 105 / 150 / 195 / 240")
          embed.set_thumbnail(url="https://ww.namu.la/s/33d37304e47d368def6d46d26b2b554dfefa1ca695607503028b5d5fe0387bb2dcc74a9e0e353e50e3650e8f70c6cfbadfb7dccd02bd9672ea2725b7182e0728f10cb1e395c2d8721016903f3711cf40eda483fef3088057e17b35dd94cbf362") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!케이틀린 E'): 
          embed = discord.Embed(title="90구경 투망", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 90구경 투망", value="케이틀린이 투망을 발사하여 처음으로 적중한 적을 1초 동안 50% 둔화시키고 마법 피해를 입힙니다. 케이틀린은 뒤로 밀려납니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="지정한 방향으로 투망을 발사하고, 케이틀린은 그 반대 방향으로 밀려납니다. 이동 거리는 대략 점멸과 비슷한 수준 입니다.", inline=False) 
          embed.set_footer(text="16초 / 14.5초 / 13초 / 11.5초 / 10초")
          embed.set_thumbnail(url="https://w.namu.la/s/2ff1edfac1dd57064cd5040bf0b86b5f12aa0848b535d9e56b7e99d65644da6a386ad2804a5d9bb42b5122229eb38e6f83605c8b82710059a754385f99e422fe6a9b402b60a25766364ec37fe15cb213ca0e39f1a726b7c444e7f7211869a1cd") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!케이틀린 R'):
          embed = discord.Embed(title="비장의 한 발", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 비장의 한 발", value="케이틀린이 잠시 정신을 집중하고 공을 들인 완벽한 사격을 하여 물리 피해를 입힙니다. 다른 적 챔피언이 총알을 대신 맞을 수도 있습니다. 정신을 집중하는 동안 대상에 대한 절대 시야를 얻습니다.", inline=False)           
          embed.add_field(name="스킬 효과", value="사용 시 대상에 대한 절대 시야를 얻으며 1.5초 동안 정신을 집중한 뒤 대상에게 유도되는 탄환을 쏩니다. 타겟팅이지만 다른 상대 챔피언이 대신 맞을 수 있습니다. 조준하는 동안 CC기에 걸리거나 대상이 죽었거나 점멸을 사용하였을 경우 궁극기 시전이 취소됩니다.", inline=False) 
          embed.set_footer(text="90초 / 75초 / 60초")
          embed.set_thumbnail(url="https://w.namu.la/s/d090ef09bcc1deffc4af7c9f29463e856d4a42747667a28ac792eac42645d5e6ac5d8549c547d0938f34e31b03cac5cf0d98fd4d02ea6be3394ea16f1765240db69dfa950cb103c6afcf0ca067744fd43d159cfef71a976fa938a1f4b68dd1c1")
          await message.channel.send(embed=embed)
 
    elif message.content.startswith('!카이사 패시브'):
          embed = discord.Embed(title="두 번째 피부", description=" ", color=0xAAFFFF) 
          embed.add_field(name="부식성 흉터", value="카이사의 기본 공격이 4초 동안 플라즈마 중첩을 남기며 추가 마법 피해를 입힙니다. 4중첩에 도달하면 카이사가 공격했을 때 플라즈마가 폭발하며 대상이 잃은 체력에 비례한 추가 마법 피해를 입힙니다.", inline=False) 
          embed.add_field(name="살아있는 무기", value="카이사의 피부는 카이사의 공격 스타일에 적응해 아이템과 챔피언 레벨 업으로 얻는 영구 능력치를 기반으로 스킬을 진화시킵니다.", inline=False)  
          embed.set_thumbnail(url="https://ww.namu.la/s/50b8da130e5bb427eef4b706074695c505f730c53f78f5332c7ef1cba325a15bcdb669f47971d41fac76ecca4ff460d108cbc883cacdc3d59dbd392f05565a02b44717bc9b4967cea1eee56f1d533fbc84db892bf5349b6181694d5d76d0d543") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!카이사 Q'): 
          embed = discord.Embed(title="이케시아 폭우", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 이케시아 폭우", value="카이사가 근처 적들을 추적하는 미사일을 6개 발사하며, 적중한 적에게 각각 물리 피해를 입힙니다. 이미 미사일에 맞은 적 챔피언 또는 몬스터에게 추가 적중할 경우 25%의 피해를 입힙니다.", inline=False) 
          embed.add_field(name="살아있는 무기", value="진화에 필요한 추가 공격력 100 - 이케시아 폭우가 미사일을 12개 발사합니다.", inline=False) 
          embed.set_footer(text=" 10초 / 9초 / 8초 / 7초 / 6초")
          embed.set_thumbnail(url="https://w.namu.la/s/433ff6dbf1c20ad108431128e340df40e1c38b6f98ea5768cee398eadb4c5c06ac34600daee1b45c8c444cfda0648d7906ceace2dd1f23845b798e09443d5053918035a07de72c08d226d274f29612066bb95bdf4ad8f6013ce478b54a48fac0") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!카이사 W'): 
          embed = discord.Embed(title="공허추적자", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 공허추적자", value="카이사가 공허 에너지 광선을 발사해 처음으로 적중한 적에 대한 절대 시야를 얻고 광선에 적중된 대상은 플라즈마 중첩이 2회 쌓입니다. 대상은 중첩에 비례한 마법 피해를 입습니다.", inline=False)  
          embed.add_field(name="살아있는 무기", value="진화에 필요한 주문력 100 - 공허추적자가 플라즈마 중첩을 3만큼 적용하며 적 챔피언 적중 시 재사용 대기시간이 70% 감소합니다.", inline=False) 
          embed.set_footer(text="22초 / 20초 / 18초 / 16초 / 14초")
          embed.set_thumbnail(url="https://ww.namu.la/s/bd14af48b4c4a9c8f50cc33a87f3f27763625cae6c63fdd9f5d4afe1ce250463517fc7ab29bacf95aed84fa4a7608db5af72be82ca07c584529b0496980f9a4744e052acdee54021c3ea8d6516571dc661fedff99fb51250569f84fccb080dda") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!카이사 E'): 
          embed = discord.Embed(title="고속 충전", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 고속 충전", value="카이사가 1.2 ~ 0.6초[15] 동안 공허 에너지를 고속 충전합니다. 충전하는 동안 이동 속도가 증가하며, 충전을 마친 후 4초 동안 공격 속도가 증가합니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="기본 공격 시 고속 충전의 재사용 대기시간이 0.5초씩 감소합니다. 공격 속도가 증가할수록 고속 충전의 충전 시간은 짧아지고 이동 속도 증가량은 높아집니다.", inline=False) 
          embed.add_field(name="살아있는 무기", value="진화에 필요한 공격 속도 100% - 고속 충전을 사용하면 0.5초 동안 투명 상태가 됩니다.", inline=False) 
          embed.set_footer(text="16초 / 15초 / 14초 / 13초 / 12초")
          embed.set_thumbnail(url="https://ww.namu.la/s/4b426128820d311c774e64967560efd40840e29d7b154c52b6e503fb07262541ca92b2d2440cafadb3a5b44e6c7200acb121bcfcf2fb9837298670dd3acd683fe2da3e01ad7742891261b496249d7a12416f035800ef448e7ea4398148a451c4") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!카이사 R'):
          embed = discord.Embed(title="사냥본능", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 사냥본능", value="카이사가 플라즈마 표식이 남은 적 챔피언 근처로 빠르게 돌진하며, 2초 동안 피해를 흡수하는 보호막을 얻습니다.", inline=False)           
          embed.set_footer(text="130초 / 100초 / 70초")
          embed.set_thumbnail(url="https://ww.namu.la/s/f0ac6617755110fd6288a6cbb993787de91bf81fccfec8c12b9dd66285035b213206582ebedb67965c4c0c81600ee5e68247f6952b9560d8f9de9fc1d73777a8175aa2797627374e6949241a0f6c9ce87c417da31426a48d6238565d12f85179")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!자야 패시브'):
          embed = discord.Embed(title="관통상", description=" ", color=0xAAFFFF) 
          embed.add_field(name="관통상", value="스킬을 사용 후 다음 3회 기본 공격이 경로에 있는 모든 적에게 피해를 입히고 6초 동안 유지되는 깃털을 남깁니다.", inline=False) 
          embed.add_field(name="연인의 귀환", value="자야와 라칸은 동시에 귀환할 수 있습니다.", inline=False)  
          embed.set_thumbnail(url="https://w.namu.la/s/bb34504050512421dd49b0d1c2bc13481921a90b58422ae6f098e6c55ee42866fa7a4ee0cc27328d25c9dd00c16b583b849e8516fd993c848e37140db51a08dbc5b5128151a55a8a976ca02db7b4ef95450203e6d724a0c9ec701248364b5aaf") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!자야 Q'): 
          embed = discord.Embed(title="깃털 연타", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 깃털 연타", value="자야가 연타 공격을 가해 물리 피해를 입히고 깃털 두 개를 남깁니다. 두 번째 대상부터는 단검 하나당 50%의 피해를 입힙니다.", inline=False) 
          embed.set_footer(text=" 10초 / 9초 / 8초 / 7초 / 6초")
          embed.set_thumbnail(url="https://w.namu.la/s/4e94144f9db7d2f4478a4d3a03aa8dede6bbe722f8e6c5e6ca0b8c0f29b6a9a5f8ce2b873b02d231bebb98d8b01e070e8ae56a3b79f004ee19a524cd17b17fa0c1f434c8a6abd78309cb0a11738c379389ba081278c91d6a51f337d60506e1aa") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!자야 W'): 
          embed = discord.Embed(title="죽음의 깃", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 죽음의 깃", value="자야가 4초 동안 칼날 폭풍을 일으켜 공격 속도가 상승하고 기본 공격 시 두 번째 칼날을 날려 20%의 피해를 입힙니다. 두 번째 칼날이 챔피언에게 적중하면 1.5초 동안 자야의 이동 속도가 30% 상승합니다.", inline=False)  
          embed.add_field(name="추가 효과", value="라칸이 근처에 있으면 함께 이 스킬의 효과를 받습니다. 단 자야가 대상을 공격해야 라칸의 이동 속도가 상승합니다.", inline=False) 
          embed.set_footer(text="20초 / 19초 / 18초 / 17초 / 16초")
          embed.set_thumbnail(url="https://w.namu.la/s/ca7abbc479694119e371b336778f777790e4ce216be7c5c70f321dbac141fec9d4a5b3e9d7247e20aebd4efbbae2c2822e3b66bc5156be9765a952c75e0ecf87fe814bbc8898d1ffe31b8a36073981bce2d8b38e1a6e30bfb9b7ab468543e457") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!자야 E'): 
          embed = discord.Embed(title="깃부르미", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 깃부르미", value="자야가 모든 깃털을 불러들여 각 깃털로 물리 피해를 입힙니다. 피해량은 치명타 확률에 따라 증가합니다. 적이 3개 이상의 깃털에 맞으면 1.25초 동안 속박됩니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="미니언 상대로는 50%의 피해를 입힙니다.적은 깃털에 맞을 때마다 받는 피해가 5%씩 감소하여 최소 10%의 피해를 받습니다.", inline=False) 
          embed.set_footer(text="10초 / 9.5초 / 9초 / 8.5초 / 8초")
          embed.set_thumbnail(url="https://w.namu.la/s/1807775dcfb62b0b6a09ea6bc7441e68bffd91d44f6b7074844210c8811b5fccb377a98235aed4dbea802a2f0e408f9e76b2fff7565ab26339f511f4c416cd1b109be2217b1056526a13b12154eb18994bdfcba04ca4c216115816ce8498c07f") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!자야 R'):
          embed = discord.Embed(title="저항의 비상", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 저항의 비상", value="자야가 공중으로 도약해 1.5초 동안 대상으로 지정할 수 없는 유체화 상태가 된 후 원뿔 모양으로 공격을 가해 물리 피해를 입히고 일렬로 깃털을 남깁니다.", inline=False)           
          embed.add_field(name="스킬 효과", value="대상으로 지정할 수 없는 유닛은 이미 영향을 받은 상태가 아닌 한 적의 기본 공격이나 스킬에 영향을 받지 않습니다.유체화 상태인 유닛은 다른 유닛과 충돌하지 않습니다.자야는 공중에 뜬 상태로 움직일 수 있습니다.", inline=False)
          embed.set_footer(text="140초 / 120초 / 100초")
          embed.set_thumbnail(url="https://ww.namu.la/s/4b13a647fc8b9fa60f485d5f07e908d22818cbfc48f136c9a2781103de3ee1f8790da4456558e0f13c3d1abfa0381daeca8cfa98b9fa4b7dae691fed648675537d0e141b613b8945bc4f5ae80c32f737fc610f3ef95555d4362b0fd355061cbe")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!시비르 패시브'):
          embed = discord.Embed(title="재빠른 발놀림", description=" ", color=0xAAFFFF) 
          embed.add_field(name="재빠른 발놀림", value="시비르가 기본 공격이나 스킬로 적 챔피언을 공격하면 2초 동안 이동 속도를 얻습니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/6e062b51e644eabf0229816e1397ef710324e96dac33d5808df4f8948b8ccb20382412c4fccbaedef1d5dd0e93dcb47468cdc55e1abd62eda07127148a0cb795662500988a01f061b49173a4d1dc786ddfaf6d5e4ae2979eb1345ad963928096") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!시비르 Q'): 
          embed = discord.Embed(title="부메랑 검", description=" ", color=0xAAFFFF)  
          embed.add_field(name="Q - 부메랑 검", value="시비르가 십자날 검을 던져서 관통하는 모든 적 챔피언에게 물리 피해를 입히고 돌아오며 두 번째 피해를 입힙니다. 이 스킬은 챔피언이 아닌 대상에게 적중할 때마다 피해량이 15%씩 감소하며 최소 40%까지 내려갈 수 있습니다.", inline=False) 
          embed.add_field(name="추가 효과", value="십자날 검이 돌아올 때 피해량 감소는 초기화됩니다.", inline=False) 
          embed.set_footer(text="7초")
          embed.set_thumbnail(url="https://w.namu.la/s/dd161d0ad3f036c3d979e13f436979af377ffc4fcb811d93c1f95f82fc8eeaf4b6d2a6d994abbcca3d282af8989a4cf99b1a39a1b5c58f79afb78cd9a9a9da7712caab8be6ccc5696070217773b7edf20e7d19ed4f3ca0645ba856d0600fc23e") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!시비르 W'): 
          embed = discord.Embed(title="튕기는 부메랑", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 튕기는 부메랑", value="시비르의 다음 기본 공격 3회는 주변 대상에게 튕기며 첫 번째 대상에게는 100% 공격력의 물리 피해를, 그다음 대상에게는 각각 감소된 물리 피해를 입힙니다. 첫 번째 대상에게 치명타로 적중 시 튕긴 대상에게도 치명타로 적중됩니다.", inline=False)  
          embed.add_field(name="추가 효과", value="튕기는 부메랑 스킬은 같은 대상을 한 번 이상 맞힐 수 없습니다.", inline=False) 
          embed.set_footer(text="12초 / 10.5초 / 9초 / 7.5초 / 6초")
          embed.set_thumbnail(url="https://w.namu.la/s/f81f30efb2d12a2002f1473f8c22dee3d4ca1a164a3286ae3001473b53cb6c19cefef4815df75fd6d4d0d6f2ede9c74cbf25929e51419d674c20b03769361958afa1a9c42c503cef2dca837a96ce6b398c1334a4714bdd8f988a3d56331b1da5") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!시비르 E'): 
          embed = discord.Embed(title="주문 방어막", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 주문 방어막", value="시비르가 1.5초간 주문 방어막을 만들어 적의 스킬을 막아냅니다. 적의 스킬을 방어하는 데 성공하면 시비르가 마나를 회복합니다.", inline=False) 
          embed.add_field(name="스킬 효과", value="이 보호막은 챔피언과 아이템 스킬을 모두 방어합니다.", inline=False) 
          embed.set_footer(text="22초 / 19초 / 16초 / 13초 / 10초")
          embed.set_thumbnail(url="https://w.namu.la/s/1c4c5f7f0296bf2aa5ee2df1ddd4a83aeba79361d6bbb1f067dc57c80c1929dc64a6d030b352dfdebc44022a477dd99a81cd3bc407803eb22cf3e9c8b95f81efb6b11ce69cb73e80fbf060d66d4c4f6528a7ae29d0c38ff712f9498b7eefcc00") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!시비르 R'):
          embed = discord.Embed(title="사냥 개시", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 사냥 개시", value="기본 지속 효과: 튕기는 부메랑이 활성화된 상태에서 시비르의 공격 속도가 증가합니다.", inline=False)           
          embed.add_field(name="스킬 효과", value="사용 시: 시비르가 8초 동안 아군을 규합하여, 주변 모든 아군의 이동 속도가 증가합니다. 이 효과는 몇 초에 걸쳐 점점 약해집니다.", inline=False)
          embed.set_footer(text="120초 / 100초 / 80초")
          embed.set_thumbnail(url="https://w.namu.la/s/9a65d9c7c4eccb1185d03558d2d17139a845a409ded105cd23e283b1147937f7b5c556a11e5c64ff6b0828f439b332a2842674088b88ca1405d700a5a22235a7e40151dc24aa7fcbcca1020677fd8a6f92382b82e7c3ca5b8131bf03902b2910")
          await message.channel.send(embed=embed)
          
    elif message.content.startswith('!징크스 패시브'):
          embed = discord.Embed(title="신난다!", description=" ", color=0xAAFFFF) 
          embed.add_field(name="신난다!", value="징크스가 챔피언이나 에픽 몬스터, 구조물에 피해를 입힌 뒤 3초 안에 해당 챔피언, 에픽 몬스터가 처치되거나 구조물이 파괴되면 6초간 징크스의 공격 속도가 15% 증가하고 이동 속도가 175% 증가했다가 점차 감소합니다. 신이 난 징크스는 최고 공격 속도 제한을 초과할 수 있습니다.", inline=False) 
          embed.set_thumbnail(url="https://ww.namu.la/s/e6f767dcf3dd19c493186e1f75febfde4b2bc186b709687e21fadb1905dfd9026530d31c2610a011e33ebeb4223a3ac28b79d32f5b9596df30b0b97801aeee1f5947b7e7f4c41138aa0558c656613a30ef8c3a5198e64beeb539b69e38c628c1") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!징크스 Q'): 
          embed = discord.Embed(title="휘릭휘릭!", description=" ", color=0xAAFFFF)  
          embed.add_field(name="생선 대가리 로켓 런처", value="로켓 런처로 기본 공격 시 마나를 소모하여 대상과 주변 적들에게 110%의 물리 피해를 입힙니다. 추가 공격 속도는 10% 느려지지만 사거리는 증가합니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/3d1fc05a5cc75e0fc9bf5cb2fb0ebfc2019b1d6c3c40abb3717f9276d812237a9c33f93a228e6cd84cf89b4c3d6d53050ecfb144fabe9a38ff7b52774aec369043d0aa2b62672607f64a597fed289127062fd0b16af9c346b90e89f1be38d28b") 
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="휘릭휘릭!", description=" ", color=0xAAFFFF)  
          embed.add_field(name="빵야빵야 미니건", value="미니건으로 기본 공격 시 2.5초 동안 공격 속도가 상승합니다. 이 효과는 최대 3번까지 중첩됩니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/72bd4ce2f61b30a3a24178cea4d5f82ccf6ff7ec703275a324b82ee1b28560b28ddfd14b2499c101637d12bd33a5e8d73317236bc81778c08bb3dc2f20f68e3514abc0f9d278131aef570a88f5a555f89ca777188432467c423cac52736163c1") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!징크스 W'): 
          embed = discord.Embed(title="빠직!", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 빠직!", value="징크스가 전기 충격파를 발사하여 처음 맞힌 적에게 물리 피해를 입히고, 2초 동안 둔화시키며 위치를 드러냅니다.", inline=False)  
          embed.set_footer(text="8초 / 7초 / 6초 / 5초 / 4초")
          embed.set_thumbnail(url="https://ww.namu.la/s/15ffe2a3312a03d9c943eb3bd048f20f9a4e9376ad7b263bef3bc24133bb61b02b99af9ed6c4211485e65f3ff1b3eeebb893256452315e63b4eb4f5aa731ab00239c1d507a60db26ce13e0a381e2446bfbecb50839015ed4e5094d959a4da613") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!징크스 E'): 
          embed = discord.Embed(title="와작와작 뻥!", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 와작와작 뻥!", value="징크스가 5초간 유지되는 와작와작 지뢰 3개를 던집니다. 적 챔피언이 닿으면 1.5초 동안 롤아이콘-군중제어 속박속박시키고 폭발하여 주변 적들에게 마법 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="24초 / 20.5초 / 17초 / 13.5초 / 10초")
          embed.set_thumbnail(url="https://ww.namu.la/s/7c62fd1b3eb3e7a60ad79d277e7eb741cf53b39a87bd29bf1b85575bf302b85d3cf42baa7e8f989af5e95c02a5cc217d949745de5da8f9a2cb15c2990c83789dc5bba3f7b0184676ecf14d91548c227a73cefadff049ef56ca98e45326ace343") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!징크스 R'):
          embed = discord.Embed(title="초강력 초토화 로켓!", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 초강력 초토화 로켓!", value="징크스가 로켓을 발사합니다. 로켓은 발사 후 첫 1초 동안 피해량이 커지며, 적 챔피언을 맞히면 폭발하여 물리 피해를 입힙니다. 주위의 적들은 80%의 피해를 입습니다.", inline=False)           
          embed.add_field(name="스킬 효과", value="사용 시: 시비르가 8초 동안 아군을 규합하여, 주변 모든 아군의 이동 속도가 증가합니다. 이 효과는 몇 초에 걸쳐 점점 약해집니다.", inline=False)
          embed.set_footer(text="90초 / 75초 / 60초")
          embed.set_thumbnail(url="https://ww.namu.la/s/2e316ac151c86186ebe0eefe5d82f3dd3374f4fae76907dbeb558fa4ca181874962b235b765466519f32eea22a4a2da20ffecda884398b6cb5e23ebca8dc25ba30988e26a4b6fc462269f8db6d724db4e129350bb83727533e3f61eff84e16fb")
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!이즈리얼 패시브'):
          embed = discord.Embed(title="끓어오르는 주문의 힘", description=" ", color=0xAAFFFF) 
          embed.add_field(name="끓어오르는 주문의 힘", value="이즈리얼이 스킬을 적중시키면 6초 동안 공격 속도가 10% 증가합니다. 이 효과는 최대 5번 중첩됩니다.", inline=False)  
          embed.set_thumbnail(url="https://w.namu.la/s/3380f1d01729c9a4edbab98c70f0173da21324d0b333c1187619bc135698f051afd3e31e5052281a53719a591486568c845dbd01e3706dd072189d0c77eba35a72f88ecbba2ed0097c008d07ffee5e7398187f8bec92fff83de05695d4cc3b98") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!이즈리얼 Q'): 
          embed = discord.Embed(title="신비한 화살", description=" ", color=0xAAFFFF)  
          embed.add_field(name="신비한 화살", value="이즈리얼이 에너지 화살을 발사하여 처음 적중한 적에게 물리 피해를 입히고, 이즈리얼의 스킬 재사용 대기시간을 1.5초 감소시킵니다(적중 시 효과 적용)", inline=False) 
          embed.set_footer(text="5.5 초 / 5.25초 / 5초 / 4.75초 / 4.5초") 
          embed.set_thumbnail(url="https://ww.namu.la/s/c3c18c7c64084837a88d63d752bf931e10bd87b2112f947f9cda0a6ae4ff312fdba4e04c1d84b464445d4906d14579af201604b225728b45709e530138f2b8535952e1117230ba22507a2a61595d6c375beb948e7cc7a96dc8d573b2ff74c492") 
          await message.channel.send(embed=embed)
          
    elif message.content.startswith('!이즈리얼 W'): 
          embed = discord.Embed(title="정수의 흐름", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 정수의 흐름", value="이즈리얼이 마법의 구체를 발사해 처음으로 적중한 챔피언이나 구조물, 에픽 정글 몬스터에게 4초 동안 남아있게 합니다.", inline=False)  
          embed.set_footer(text="12초")
          embed.set_thumbnail(url="https://ww.namu.la/s/78208350649df3c05cbf7b41a83c15cc403a668278131f9e680d7c8efb48b0e1290fd6b0bf15ee0a93de00d0ac944d8283e76c71c8d610cea8f5e61cafd8eac7bcc4cc0327fa700501f9c5111450f34d95936c0716f345cd514b48dd0d73a738") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!이즈리얼 E'): 
          embed = discord.Embed(title="비전 이동", description=" ", color=0xAAFFFF)  
          embed.add_field(name="E - 비전 이동", value="이즈리얼이 순간이동 후 가장 가까이에 있는 적에게 화살을 발사하여 마법 피해를 입힙니다. 화살은 정수의 흐름에 영향을 받은 대상을 우선적으로 공격합니다.", inline=False) 
          embed.set_footer(text="28초 / 25초 / 22초 / 19초 / 16초")
          embed.set_thumbnail(url="https://ww.namu.la/s/62aad5c2ab81f0c54f1dbed3afb95332b5c173c0dd5ad57dbed4a7f4a809f1bad4d2b4ee357c80228a6b977696d619d79164e74241ce5007e923b76034c64248d006b55d5ee3a1eb6750e1f4c49eefd7524fd3932c980695a584f3f4d35f40b6") 
          await message.channel.send(embed=embed)
      
    elif message.content.startswith('!이즈리얼 R'):
          embed = discord.Embed(title="정조준 일격", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 정조준 일격", value="이즈리얼이 거대한 에너지파를 발사하여 마법 피해를 입힙니다. 에픽 몬스터를 제외한 미니언과 정글 몬스터에게는 50%의 피해를 입힙니다.", inline=False)           
          embed.set_footer(text="120초")
          embed.set_thumbnail(url="https://ww.namu.la/s/4a797e18078c27804947677a1de28ad206c16edfa4dfd09922d5bf47da80fb9af5261720b40f3db3ac7d175487b5333daf5aa31e8fe371ff3059944f9823543556dd027016572a14acc79b262af633ba5e502aa3744d28d7ca37e24bb838b4b8")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!아펠리오스 패시브'):
          embed = discord.Embed(title="암살자와 예언자", description=" ", color=0xAAFFFF) 
          embed.add_field(name="무기의 달인", value="한 번에 주 무기와 보조 무기 등 총 두 가지 무기를 사용할 수 있습니다. 각 무기는 고유의 기본 공격과 [Q] 스킬을 가지고 있습니다. 기본 공격과 스킬 사용 시 탄약을 소모하며, 탄약을 모두 소모하면 사용 중인 주 무기를 다음 무기로 교체합니다. 아펠리오스는 스킬 포인트로 스킬 레벨을 올리는 대신 영구 능력치를 획득합니다.", inline=False)  
          embed.add_field(name="무기 순서", value="만월총 (소총): 사거리 추가\n절단검 (낫 모양 권총): 생명력 흡수 및 이동 속도 증가\n중력포 (대포): 둔화 + 이동 불가 효과\n화염포 (화염 방사기): 광역 피해\n반월검 (투척 무기): 근거리에서 공격할수록 강력한 피해", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/71f2ab02742ac01a498d5a5379bb4dffec1c42338c9ba3da577af6e4199d3a980c37efdf791ee0939c04c72b791eb22419243a2acd05e2d77e49b826ee1b27fd585ecc7cdff9d130c745e733079a9b5763e1791b76f17e5b97c9295f1e9de1a1") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!아펠리오스 만월총'): 
          embed = discord.Embed(title="저격소총", description=" ", color=0xAAFFFF)  
          embed.add_field(name="만월총 기본 지속 효과", value="아펠리오스의 공격 사거리가 100 상승합니다.", inline=False) 
          embed.add_field(name="만월총 효과", value="만월총을 사용하는 스킬은 4.5초 동안 대상에게 표식을 남기고 위치를 드러냅니다. 표식이 있는 대상은 먼 거리[18]에서 보조 무기로 공격할 수 있습니다. 대상 공격 시 주변의 모든 표식을 소모하여 표식 1개당 추가 물리 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="보조 무기가 만월총인 경우 주 무기를 사용하여 공격합니다.")
          embed.set_thumbnail(url="https://w.namu.la/s/1e8f8c79218d8a9ddba1487708a8ca530e67309d3797f6903b1ccfe8af26e8df26796cde4d83e8f61ebb71338a3c784930057acf0d606b4be9e686d9dd4605b073139e908d50539acbfdb98865c191041d460a1393c7c8eef6a1a2ce6cf4f3d8") 
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="만월총 Q", description=" ", color=0xAAFFFF)  
          embed.add_field(name="달빛탄", value="만월총 사용 시: 원거리 공격을 가하여 처음 적중한 적에게 물리 피해를 입히고 표식을 남깁니다.", inline=False) 
          embed.add_field(name="만월총 효과", value="만월총을 사용하는 스킬은 4.5초 동안 대상에게 표식을 남기고 위치를 드러냅니다. 표식이 있는 대상은 먼 거리[18]에서 보조 무기로 공격할 수 있습니다. 대상 공격 시 주변의 모든 표식을 소모하여 표식 1개당 추가 물리 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="10초 / 9.7초 / 9.3초 / 9초 / 8.7초 / 8.3초 / 8초 \n1 / 3 / 5 / 7 / 9 / 11 / 13레벨")
          embed.set_thumbnail(url="https://w.namu.la/s/7abef7c39852600f9c5f2ee8c0415a93e6b185967df50d50c66943eafd7b8df801f1f2bfde7841fd27c5cab4c296f259fb9830c8e2e1a1afc5736b7d07685b72be3b4e244ec4cd71d8b7a72be4352c1572c9791ae2fd95ed557f817e074af044") 
          await message.channel.send(embed=embed)
          
    elif message.content.startswith('!아펠리오스 절단검'): 
          embed = discord.Embed(title="낫 모양 권총", description=" ", color=0xAAFFFF)  
          embed.add_field(name="절단검 기본 지속 효과", value="아펠리오스가 이 무기로 입히는 피해의 일부만큼 체력을 회복합니다. 이 무기로 최대 체력 이상 체력을 회복할 경우 보호막을 얻습니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/1b77434f311c68c63352472c35a0e278e4732b4d3a3df1e48d5bdbfea108ac1fcf5129774c348c0186cb50c0310e78764aa58d37c32aaf9b5fe8af5a3aceb9101913cebabdeaf702817ca930d4db1d6e2be8ae689a3764cd64e71a64bdd06ce5") 
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="절단검 Q", description=" ", color=0xAAFFFF)  
          embed.add_field(name="맹공", value="절단검 사용 시: 아펠리오스가 이동 속도를 얻고 가장 가까운 적에게 1.75초 동안 두 가지 무기를 발사합니다. 몇 회 사격하여 물리 피해를 입힙니다. 챔피언을 우선 공격합니다.", inline=False) 
          embed.add_field(name="만월총 효과", value="만월총을 사용하는 스킬은 4.5초 동안 대상에게 표식을 남기고 위치를 드러냅니다. 표식이 있는 대상은 먼 거리[18]에서 보조 무기로 공격할 수 있습니다. 대상 공격 시 주변의 모든 표식을 소모하여 표식 1개당 추가 물리 피해를 입힙니다.", inline=False) 
          embed.set_footer(text="10초 / 9.7초 / 9.3초 / 9초 / 8.7초 / 8.3초 / 8초 \n1 / 3 / 5 / 7 / 9 / 11 / 13레벨")
          embed.set_thumbnail(url="https://ww.namu.la/s/7f9650c35cf7e29f9913e903f55976a77821da54192abc87c01ba8c63eeccb954806d23654cb465786d6964b4245397cf04ae730e49045bb8a84cc3c49e3f09cc16c049c5287fb4e5a699ba12f08991fb62ffe50dddea20b2e7ec344eb4353a1") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!아펠리오스 중력포'): 
          embed = discord.Embed(title="대포", description=" ", color=0xAAFFFF)  
          embed.add_field(name="중력포 기본 지속 효과", value="공격 시 대상을 30%만큼 둔화시킵니다. 둔화 효과는 3.5초에 걸쳐 점차 사라집니다.", inline=False) 
          embed.set_thumbnail(url="https://ww.namu.la/s/caed1b67b6d3703461d632e1d4d206176b9afa1a2bddf43be1a144ecadaeb70ac9623a17013cfdee5301126f7f5cab584d5eb54bdcb845357272e76cc25757d05a0555d1e9d1b7433b1a873f0274d728aaa7bfd92c0e77f10f2aa0189eeba7b1") 
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="중력포 Q", description=" ", color=0xAAFFFF)  
          embed.add_field(name="월식", value="중력포 사용 시: 중력포를 사용해 둔화시킨 적들에게 중력장을 펼쳐 적들을 1초 동안 속박하고 마법 피해를 입힙니다.", inline=False) 
          embed.add_field(name="추가 효과", value="이 스킬은 아펠리오스의 보조 무기가 사용되지 않습니다.", inline=False) 
          embed.set_footer(text="12초 / 11.7초 / 11.3초 / 11초 / 10.7초 / 10.3초 / 10초 \n1 / 3 / 5 / 7 / 9 / 11 / 13레벨")
          embed.set_thumbnail(url="https://w.namu.la/s/00c3fb3f331c25f64a104efdce46b08adf19b27d056fdfcb3bf47cfd5ea3b5194c17081a532ffd0c8fda798d0e86135698204920f40bf2b95edaecf0f3f99a544ee0ee5bfd352dbccf81685225ef287577b86e698f3133eb1c6f9ab7db2c1611") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!아펠리오스 화염포'): 
          embed = discord.Embed(title="화염 방사기", description=" ", color=0xAAFFFF)  
          embed.add_field(name="화염포 기본 지속 효과", value="화염포 기본 지속 효과: 아펠리오스의 공격이 첫 번째 대상에게 110%의 물리 피해를 입히고 그 뒤에 있는 모든 적에게 75% / 100%(1 레벨/9 레벨)의 피해를 입힙니다.", inline=False) 
          embed.set_thumbnail(url="https://ww.namu.la/s/44fe9cc60c81510d5a7b00467c16b77e8071aab5570f1974b1f351ee286dc019a61e278a8b0bc656de9413e38cc52196fd9a61a5f4f50a647d6ee16a4cc7a3fdd7b551cf41053f49806e78cc8b7db9e3a27842db6d5f80ab201382d6109798a3") 
          embed.set_footer(text="되돌아오는 속도는 공격 속도에 비례하여 증가합니다.")
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="화염포 Q", description=" ", color=0xAAFFFF)  
          embed.add_field(name="황혼파", value="화염포 사용 시: 화염의 파도를 발사해 적에게 물리 피해를 입힌 후 적중한 모든 적을 보조 무기로 공격합니다.", inline=False) 
          embed.set_footer(text="9초 / 8.5초 / 8초 / 7.5초 / 7초 / 6.5초 / 6초 \n1 / 3 / 5 / 7 / 9 / 11 / 13레벨")
          embed.set_thumbnail(url="https://ww.namu.la/s/acce860595bee50db395ee1b43f30bf0e08946f6a0b118269653e25844f33f026f55d84531c23e9f4b0a28b524ed05ae4f1c6585dcd00e64bb12fe44a38e538cb0a05a09fc0723757421e454674c463caa9d8c9b8ea83312fe80885978225586") 
          await message.channel.send(embed=embed)

    elif message.content.startswith('!아펠리오스 반월검'): 
          embed = discord.Embed(title="투척 무기", description=" ", color=0xAAFFFF)  
          embed.add_field(name="반월검 기본 지속 효과", value="공격 시 대상에게 반월검을 날립니다. 반월검은 아펠리오스에게 다시 돌아오며, 돌아온 즉시 다시 공격할 수 있습니다. ", inline=False) 
          embed.set_thumbnail(url="https://ww.namu.la/s/cd908bceaa2fb6a2b22e0030a2a5cb8d8e671b2e521e2f407a7e9cc52cf0776aee529c42eb0aaa883333b5cadbe815e88a6c75578986ac29e6725365eb3a8519f70081268e70bf1db1851a2d6864f3909bc3e48ddd24ce87aa9e3635fa213f8c") 
          embed.set_footer(text="되돌아오는 속도는 공격 속도에 비례하여 증가합니다.")
          await message.channel.send(embed=embed)
          embed = discord.Embed(title="반월검 Q", description=" ", color=0xAAFFFF)  
          embed.add_field(name="파수탑", value="반월검 사용 시: 아펠리오스의 보조 무기를 장착한 달빛 파수탑을 배치합니다. 파수탑은 20초 동안 지속되며, 적이 접근하면 활성화되어 4초 동안 공격 1회당 물리 피해를 입힙니다.", inline=False) 
          embed.add_field(name="추가 효과", value="이 스킬은 아펠리오스의 보조 무기가 사용되지 않습니다.", inline=False) 
          embed.set_footer(text="9초 / 8.5초 / 8초 / 7.5초 / 7초 / 6.5초 / 6초 \n1 / 3 / 5 / 7 / 9 / 11 / 13레벨")
          embed.set_thumbnail(url="https://ww.namu.la/s/5528dbc5ff8d31a76fae8bc63b95c1701f77f40dc89450a923121221c43a7a60bfa3661dfd381f3ded9a37f728b268ca964bb2876f313181d2770935c618e1fa4067c8913d3023aba085b289cc81cd29fafef64e6862e3ca36b70bb5d9f9d781") 
          await message.channel.send(embed=embed)
    
    elif message.content.startswith('!아펠리오스 W'): 
          embed = discord.Embed(title="위상 변화", description=" ", color=0xAAFFFF)  
          embed.add_field(name="W - 위상 변화", value="주 무기와 보조 무기를 교체하여 장착합니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/d8c355104229a37aea22f7e5dc2eee689938644e4948dc4bda63cf90718f9eaf815404390d5a23f89fd9feb10be2375771c7ed5e1919c2a392552830df2861730ff32498804076e36b1e209cfef4d08d98439a67fac54babbf0b28f5341ed88a") 
          embed.set_footer(text="0.8초")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!아펠리오스 R'):  
          embed = discord.Embed(title="월광포화", description=" ", color=0xAAFFFF)  
          embed.add_field(name="R - 월광포화", value="챔피언에게 적중 시 폭발하는 달빛 에너지를 발사하여 주변 적에게 물리 피해를 입힙니다. 이후 적중한 모든 챔피언을 주 무기로 공격합니다.", inline=False) 
          embed.add_field(name="상세 효과", value="만월총 추가 효과: 이 효과로 남긴 표식은 소모 시 추가 물리 피해를 입힙니다.\n절단검 추가 효과: 체력을 회복합니다.\n중력포 추가 효과: 둔화 효과가 99%까지 증가합니다. 해당 대상에게 속박의 월식의 속박 효과는 1.35초로 늘어납니다.\n화염포 추가 효과: 폭발한 달빛 에너지는 추가 물리 피해를 입히며, 후속 공격은 폭발해 주변 대상들에게 90%의 피해를 입힙니다.\n반월검 추가 효과: 반월검 환영 5개를 추가로 소환합니다.", inline=False) 
          embed.set_thumbnail(url="https://w.namu.la/s/21fa476233cd86d0d358695a1d90ff749eabdebeea0398ef6fa4c84440e44806e5a510391f480d4dc5e1759f92263ed865a0d8d136b6ed6c01dd7a694b217203d03896b2c642466b2ef04f6c7e261d9abd65ebed4993c3df4c630eb380f35412") 
          embed.set_footer(text="120초 / 110초 / 100초")
          await message.channel.send(embed=embed)

    elif message.content.startswith('!애쉬'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!코그모'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!트리스타나'):
          await message.channel.send('요청하신 정보입니다!')
    
    elif message.content.startswith('!베인'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!칼리스타'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!루시안'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!바루스'):
          await message.channel.send('요청하신 정보입니다!')

    elif message.content.startswith('!세나'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!직스'):
          await message.channel.send('요청하신 정보입니다!')

    elif message.content.startswith('!카시오페아'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!스웨인'):
          await message.channel.send('요청하신 정보입니다!')
          
    elif message.content.startswith('!신드라'):
          await message.channel.send('요청하신 정보입니다!')

    elif message.content.startswith('!드레이븐'):
          await message.channel.send('요청하신 정보입니다!')
    
    elif message.content.startswith('!야스오'):
          await message.channel.send('요청하신 정보입니다!')

client.run(token)