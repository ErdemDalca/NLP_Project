# Pipeline
[![Discord](https://img.shields.io/discord/701531356609511555.svg?logo=discord&label=)](https://discord.gg/bqkrsyxwAF) [![Maven Version](https://mvnhelper.potatocorp.dev/otran-repo/us.kunet/pipeline/badge.png)](https://mvnhelper.potatocorp.dev/otran-repo/us.kunet/pipeline)

Pipeline is a library for Kotlin that simplifies step-by-step
processes into simplified "pipeline" objects.

### Pipeline by Example
The following is an example of how a pipeline could be used
to simplify the operation of an imaginary game PipelineWizard!

```kotlin
import us.kunet.pipeline.regularStep
import us.kunet.pipeline.syncPipelineOf

/*

Briefing: You were contacted by a games company to program their latest hit game, PipelineWizard! The only things
you were given were a brief game design document and a lecture to "use your creativity". PipelineWizard is a simple
fighting game that takes place in a magical universe where everyone is a wizard!

Game specifications:

WIZARDS:
    Wizards are players who possess health (full: 100) and mana (full: 100) and can deal three types of magic attacks:
    fire, wind, and water. Wizards also have the same types as their class (i.e. wind wizard).

    The following chart shows how the different type of attacks interact with each other. The arrow means that the
    attack on the left does TWICE the amount of initial damage to the wizard with the class on the right.

    Water -> Fire
    Fire -> Wind
    Wind -> Water

    - Attacks have a 10% chance of being blocked meaning they have absolutely no effect on the attacked wizard.
    - Each attack requires the consumption of 30 mana.
    - Attacks can have a bonus multiplier of up to 25% more damage!

This example seeks to demonstrate how a system like this could be implemented using Pipeline!

 */

enum class AttackType { WATER, FIRE, WIND }

class Wizard(val type: AttackType, var health: Int = 100, var mana: Int = 100) {
    fun message(message: String) = println(message)
}

class AttackEvent(
    val attacker: Wizard,
    val victim: Wizard,
    val baseDamage: Int,
    var additionalDamage: Int = 0,
    var deflected: Boolean = false
) {
    fun damageSum() = baseDamage + additionalDamage
}

// shouldRun makes the step only execute should the condition be true, it is true by default
fun manaConsumption() = regularStep<AttackEvent>(shouldRun = { attacker.mana >= 30 }) {
    attacker.mana -= 30
}

// shouldRun makes the step only execute should the condition be true, it is true by default
fun deflect() = regularStep<AttackEvent>(shouldRun = { Math.random() < 0.1 }) {
    deflected = true
    attacker.message("UNLUCKY! Your attack was deflected by the enemy wizard")
}

// dummy step other steps can rely on to see if the damage actually should happen
fun damageHappened() = regularStep(manaConsumption()::class, shouldRun = { !deflected }) {}

fun attackDoubler() = regularStep(damageHappened()::class, shouldRun = {
    attacker.type == AttackType.WATER && victim.type == AttackType.FIRE ||
            attacker.type == AttackType.FIRE && victim.type == AttackType.WIND ||
            attacker.type == AttackType.WIND && victim.type == AttackType.WATER
}) {
    additionalDamage += baseDamage
    attacker.message("You are a ${attacker.type} type and the enemy is a ${victim.type} so damage is DOUBLED")
}

fun bonusAttackDamage() = regularStep(damageHappened()::class) {
    val bonusDamage = (damageSum() * (1 + Math.random() * 0.25)).toInt()
    additionalDamage += bonusDamage
    attacker.message("BONUS DAMAGE: +$bonusDamage")
}

fun damageApplicator() = regularStep(damageHappened()::class) {
    victim.health -= damageSum()
    attacker.message("You did ${damageSum()} damage to the enemy, their health: ${victim.health}")
}

fun main() {
    val damagePipeline = syncPipelineOf(
        manaConsumption(),
        deflect(),
        damageHappened(),
        attackDoubler(),
        bonusAttackDamage(),
        damageApplicator()
    )

    val playerOne = Wizard(AttackType.FIRE)
    val playerTwo = Wizard(AttackType.WIND)

    playerOne.message("Player 1 attack")
    println()

    // player one attacks player two with 10 damage!
    // EXPECTED: attack deals double damage due to class difference
    val attackEvent = AttackEvent(playerOne, playerTwo, 10)
    damagePipeline.channelSync(attackEvent)

    println()
    playerOne.message("END Player 1 attack, being Player 2 attack")
    playerTwo.message("Player 2 attack")
    println()

    // player two attacks player one with 10 damage!
    // EXPECTED: NO double damage happens due to class difference
    val attackEventTwo = AttackEvent(playerTwo, playerOne, 10)
    damagePipeline.channelSync(attackEventTwo)

    println()
    playerTwo.message("END Player 2 attack")
    println("Game over")
}
```
